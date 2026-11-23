# Final project

## Emotion Detection with Watson NLP and Flask

This project sends English text to the IBM Skills Network Watson NLP service and shows scores for anger, disgust, fear, joy, and sadness. The highest score determines the dominant emotion.

## Run the application

Use Python 3.9 or later. Run these commands in the project root with your Python environment active.

```sh
python -m pip install -r requirements.txt
python server.py
```

Open `http://localhost:5000` locally or launch port `5000` in the Skills Network lab. Enter `I think I am having fun` and click **Run Sentiment Analysis**. An empty input displays `Invalid text! Please try again!`.

## Verify the code

```sh
python -m unittest -v test_emotion_detection
python -m pylint server.py
```

The five tests send the reference phrases to Watson. Use the lab environment if your network cannot reach the Watson endpoint. Pylint checks the server code without calling Watson.

```python
from EmotionDetection import emotion_detector

emotion_detector("I am so happy I am doing this")
```
