import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers=header)

    formatted_response = json.loads(response.text)

    json_to_be_parsed = formatted_response['emotionPredictions']

    emotions = json_to_be_parsed[0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    score_dominant_emotion = 0
    dominant_emotion = ''

    for emotion, score in emotions.items():
        if score >= score_dominant_emotion :
            score_dominant_emotion = score
            dominant_emotion = emotion

    return (json.dumps({'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion},
            indent = 0))
