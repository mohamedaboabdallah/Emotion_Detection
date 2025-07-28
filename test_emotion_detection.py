import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_case_1(self):
        response=emotion_detector("I am glad this happened")
        comp=response['dominant_emotion']
        self.assertEqual(comp,'joy')
    def test_case_2(self):
        response=emotion_detector("I am really mad about this")
        comp=response['dominant_emotion']
        self.assertEqual(comp,'anger')
    def test_case_3(self):
        response=emotion_detector("I feel disgusted just hearing about this")
        comp=response['dominant_emotion']
        self.assertEqual(comp,'disgust')
    def test_case_4(self):
        response=emotion_detector("I am so sad about this")
        comp=response['dominant_emotion']
        self.assertEqual(comp,'sadness')
    def test_case_5(self):
        response=emotion_detector("I am really afraid that this will happen")
        comp=response['dominant_emotion']
        self.assertEqual(comp,'fear')

if __name__ == '__main__':
    unittest.main()