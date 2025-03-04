import time
from config import AUDIO_DURATION, AUDIO_FILE
import subprocess
from pydub import AudioSegment

#process = subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "-t", str(self.duration), self.audio_file_path])

class Audio:
    def __init__(self, driver):
        self.driver = driver
        self.audio_file_path = AUDIO_FILE
        self.duration = AUDIO_DURATION
    def get_audio_duration(self):
        audio = AudioSegment.from_file(AUDIO_FILE)
        return len(audio) / 1000  
    
    def play_audio(self):
        #process = subprocess.Popen(["ffplay", "-autoexit", "-nodisp", self.audio_file_path])  # command for windows 
        audio_duration=self.get_audio_duration()
        if (self.duration>audio_duration):
            self.duration=audio_duration
        process=subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "-t", str(self.duration), self.audio_file_path])
        time.sleep(self.duration)
        process.terminate() # Terminate the process if it's still running
        print(f"Playback stopped after {self.duration} seconds.")
        return 
    
