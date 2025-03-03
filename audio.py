import time
from config import AUDIO_DURATION, AUDIO_FILE
import subprocess


class Audio:
    def __init__(self, driver):
        self.driver = driver
        self.audio_file_path = AUDIO_FILE
        self.duration = AUDIO_DURATION
    def play_audio(self):
        process = subprocess.Popen(["ffplay", "-autoexit", "-nodisp", self.audio_file_path])  # command for windows 
        time.sleep(self.duration)
        print("im' here")
        # Terminate the process if it's still running
        process.terminate()
        print(f"Playback stopped after {self.duration} seconds.")
        return 
