import requests
import json

def emotion_detector(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    emotion_dict = formatted_response['emotionPredictions'][0]["emotion"]

    # Extracting emotion
    anger = emotion_dict['anger']
    disgust = emotion_dict['disgust']
    fear = emotion_dict['fear']
    joy = emotion_dict['joy']
    sadness = emotion_dict['sadness']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    return {'anger': anger, 'disgust': disgust, 'fear': fear, 'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion }