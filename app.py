from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

dataset_path = os.path.join("static", "dataset", "emotion", "train_dir")

emoji_map = {
    "angry": "😡",
    "disgust": "🤢",
    "fear": "😨",
    "happy": "😂",
    "neutral": "😐",
    "sad": "😢",
    "surprise": "😲"
}

@app.route('/')
def index():
    emotions = list(emoji_map.keys())
    selected_emotion = random.choice(emotions)
    emotion_dir = os.path.join(dataset_path, selected_emotion)
    image_filename = random.choice(os.listdir(emotion_dir))
    image_path = f"dataset/emotion/train_dir/{selected_emotion}/{image_filename}"
    correct_emoji = emoji_map[selected_emotion]

    return render_template("index.html", 
                           captcha={"image": image_path, "correct_emoji": correct_emoji}, 
                           emojis=list(emoji_map.values()))

@app.route('/validate', methods=['POST'])
def validate():
    user_emoji = request.form.get("emoji")
    correct_emoji = request.form.get("correct_emoji")

    if user_emoji == correct_emoji:
        return redirect(url_for("verified"))
    else:
        return redirect(url_for("wrong"))

@app.route('/verified')
def verified():
    return render_template("verified.html")

@app.route('/wrong')
def wrong():
    return render_template("wrong.html")

if __name__ == '__main__':
    app.run(debug=True)
