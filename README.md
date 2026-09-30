# Emotion Detection Application

## Final Project

This project implements an AI-based Emotion Detection web application using IBM Watson Natural Language Processing (NLP).

The application analyzes text and detects five emotions:

* Anger
* Disgust
* Fear
* Joy
* Sadness

It also identifies the dominant emotion.

## Features

* Emotion detection using Watson NLP
* Dominant emotion identification
* Flask web application
* Error handling for invalid input
* Unit testing
* Static code analysis using Pylint

## Technologies

* Python
* Flask
* IBM Watson NLP
* Requests
* unittest
* Pylint

## Project Structure

```text
EmotionDetection/
    __init__.py
    emotion_detection.py

templates/
    index.html

static/
    mywebscript.js

server.py
test_emotion_detection.py
README.md
```

## How to Run

Install the required packages:

```bash
pip install flask requests pylint
```

Run the unit tests:

```bash
python test_emotion_detection.py
```

Run the Flask application:

```bash
python server.py
```

Then open:

```text
http://127.0.0.1:5000/
```

