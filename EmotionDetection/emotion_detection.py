import requests
import json
def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json=obj,headers=header)
    if response.status_code == 200 :
        json_response=json.loads(response.text)
        emotions = json_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        anger_score=emotions['anger']
        disgust_score=emotions['disgust']   
        fear_score=emotions['fear']
        joy_score=emotions['joy']
        sadness_score=emotions['sadness']
        dominant_score=emotions['anger']
        return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion }
    elif response.status_code == 400 or response.status_code == 500:
        return {'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None }
