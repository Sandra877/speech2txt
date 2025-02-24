from channels.generic.websocket import WebsocketConsumer
from vosk import Model, KaldiRecognizer
import json
import numpy as np

class TranscriptionConsumer(WebsocketConsumer):
    def connect(self):
        try:
            print("Initializing Vosk model...")
            self.model = Model("vosk_model/vosk-model-small-en-us-0.15")
            self.recognizer = KaldiRecognizer(self.model, 16000)
            self.accept()
            print("WebSocket connected successfully")
        except Exception as e:
            print(f"Error in connect: {str(e)}")

    def receive(self, text_data):
        try:
            audio_data = json.loads(text_data)
            audio_array = np.array(audio_data['audio'], dtype=np.int16)
            
            # Debug info
            print(f"Received audio chunk of size: {len(audio_array)}")
            
            if self.recognizer.AcceptWaveform(audio_array.tobytes()):
                result = json.loads(self.recognizer.Result())
                if result['text']:
                    print(f"Recognized: {result['text']}")
                    self.send(text_data=json.dumps({
                        'transcript': result['text']
                    }))
        except Exception as e:
            print(f"Error processing audio: {str(e)}")

    def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}")
