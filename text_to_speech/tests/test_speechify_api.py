from django.test import TestCase
from text_to_speech.speechify_api import get_voices, tts, stream_speech


class TestSpeechify(TestCase):
    def setUp(self):
        pass

    def test_get_voices(self):
        pass
        # voices = get_voices()

    def test_stream_speech(self):
        text = "Hey there! I'm Tony, the McDonald's crypto guy. Just tryna turn this stack into a Milly, you feel me? What's up with you? 🍔💰"
        stream_speech(voice_id="tasha", text=text)

    def test_tts(self):
        text = "Hey there! I'm Tony, the McDonald's crypto guy. Just tryna turn this stack into a Milly, you feel me? What's up with you? 🍔💰"
        speech = tts(voice_id="tasha", text=text)
        print(speech.json())




