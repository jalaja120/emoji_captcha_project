from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

# CONFIGURATION
URL = "http://localhost:5000"  # Change this if your CAPTCHA is hosted elsewhere
ATTEMPTS = 10

# Setup headless Chrome browser
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)

success_count = 0

for attempt in range(ATTEMPTS):
    driver.get(URL)
    time.sleep(2)  # Wait for the page and emojis to load

    emojis = driver.find_elements(By.CLASS_NAME, "clickable-emoji")
    print(f"Attempt {attempt + 1}: Found {len(emojis)} emoji buttons.")

    if not emojis:
        continue  # Skip if emojis not found

    random.choice(emojis).click()
    time.sleep(2)  # Wait for redirect or reload

    current_url = driver.current_url
    if "verified" in current_url:
        success_count += 1
        print("✅ CAPTCHA Broken!")
    else:
        print("❌ CAPTCHA Defense Held.")

# Final report
print(f"\nSummary: {success_count}/{ATTEMPTS} successful attacks.")
driver.quit()
