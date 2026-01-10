from tts import TTS
from ocr import OCR

class Capstone(TTS, OCR):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
