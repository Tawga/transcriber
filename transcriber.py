import whisper, os
from whisper.utils import get_writer

class Transcriber:
    def __init__(self) -> None:
        self.model:str
        self.audio_filepath:str
        self.result:dict
    
    def transcribe(self, whisper_model:str, audio_fp:str, translate:bool, callback):
        self.audio_filepath = audio_fp
        self.model = whisper.load_model(whisper_model)
        self.result = whisper.transcribe(model=self.model, 
                                         audio=self.audio_filepath, 
                                         language="fi", 
                                         task="translate" if translate else "transcribe", 
                                         fp16=False)
        callback(self.result)
    
    def save_srt(self):
        path = os.path.dirname(self.audio_filepath)
        name = os.path.basename(self.audio_filepath)
        writer = get_writer("srt", path)
        writer(self.result,f"{name}")