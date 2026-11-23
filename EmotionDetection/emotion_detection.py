"""Score English text using the Watson NLP emotion model."""

import requests


WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network"
    "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return five emotion scores and the name of the highest-scoring emotion."""
    response = requests.post(
        WATSON_URL,
        json={"raw_document": {"text": text_to_analyze}},
        headers={"grpc-metadata-mm-model-id": MODEL_ID},
        timeout=15,
    )

    if response.status_code == 400:
        return dict.fromkeys((*EMOTIONS, "dominant_emotion"), None)

    response.raise_for_status()
    emotion = response.json()["emotionPredictions"][0]["emotion"]
    scores = {name: emotion[name] for name in EMOTIONS}
    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores
