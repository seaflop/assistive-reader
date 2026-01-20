from tts import TTS
from ocr import OCR
from picamera2 import Picamera2

class Capstone(TTS, OCR):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._camera = Picamera2()
        self._camera.start()
    
    def take_picture(self, image_file_location: str):
        self._camera.capture_file(image_file_location)