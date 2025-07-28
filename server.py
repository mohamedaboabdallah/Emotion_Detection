'''
This is the main server which interact using flask with the web and 
the api of emotion detector whic is implemented in Emotion Detection
Package
'''
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    '''
    this function get from user interface and show the msg 
    '''
    msg = request.args.get('textToAnalyze')
    print(msg)
    emotion_scores = emotion_detector(msg)
    if emotion_scores['anger'] is None:
        return " Invalid text!"
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
    '''
    this is the main page which appear when running our program
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5001)
