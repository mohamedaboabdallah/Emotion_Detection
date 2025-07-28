from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    msg = request.args.get('textToAnalyze')
    print(msg)
    emotion_scores = emotion_detector(msg)
    return(
        f"For the given statement, the system response is "
        f"'anger': {emotion_scores['anger']}, "
        f"'disgust': {emotion_scores['disgust']}, "
        f"'fear': {emotion_scores['fear']}, "
        f"'joy': {emotion_scores['joy']} and "
        f"'sadness': {emotion_scores['sadness']}. "
        f"The dominant emotion is {emotion_scores['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)