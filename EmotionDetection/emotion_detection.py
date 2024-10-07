import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):
    # Get NLP raw output
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)

    # Get required output in dictionary
    response_dict =  json.loads(response.text)['emotionPredictions'][0]['emotion']

    # Get dominant emotion and add to dictionary
    dominant_emotion_score = 0
    dominant_emotion = ''
    for emotion, score in response_dict.items():
        if score > dominant_emotion_score:
            dominant_emotion_score = score
            dominant_emotion = emotion
    response_dict['dominant_emotion'] = dominant_emotion

    return response_dict
