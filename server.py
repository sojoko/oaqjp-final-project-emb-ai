"""Serve the Emotion Detection interface and analysis endpoint."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException

from EmotionDetection import emotion_detector


app = Flask(__name__)
INVALID_TEXT = "Invalid text! Please try again!"


@app.route("/")
def render_index_page():
    """Render the starter project's emotion detection form."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze the submitted text and return a message for the form."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    if not text_to_analyze.strip():
        return INVALID_TEXT

    try:
        result = emotion_detector(text_to_analyze)
    except RequestException:
        return "Watson NLP is unavailable. Please try again later.", 502

    if result["dominant_emotion"] is None:
        return INVALID_TEXT

    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
