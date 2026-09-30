"""Unit tests for the EmotionDetection package."""

import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Tests that verify the dominant emotion returned by emotion_detector."""

    def test_joy_dominant(self):
        """Joy should be the dominant emotion for a clearly joyful statement."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger_dominant(self):
        """Anger should be the dominant emotion for an angry statement."""
        result = emotion_detector("I am really angry about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust_dominant(self):
        """Disgust should be the dominant emotion for a disgusted statement."""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness_dominant(self):
        """Sadness should be the dominant emotion for a sad statement."""
        result = emotion_detector("It is really sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear_dominant(self):
        """Fear should be the dominant emotion for a fearful statement."""
        result = emotion_detector("I am scared and fear this")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
