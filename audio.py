import time
from config import AUDIO_DURATION, AUDIO_FILE
import subprocess
from pydub import AudioSegment
import platform

class Audio:
    def __init__(self, driver):
        self.driver = driver
        self.audio_file_path = AUDIO_FILE
        self.duration = AUDIO_DURATION

    def get_audio_duration(self):
        """Get the duration of the audio file in seconds."""
        audio = AudioSegment.from_file(AUDIO_FILE)
        return len(audio) / 1000  
    
    def adjust_duration(self):
        """Adjust self.duration to not exceed the actual audio duration."""
        audio_duration = self.get_audio_duration()
        if self.duration > audio_duration:
            self.duration = audio_duration

    def play_audio_windows(self):
        """Play audio on Windows. Try using ffplay, and if not available, fall back to PowerShell."""
        try:
            command = ["ffplay", "-autoexit", "-nodisp", "-t", str(self.duration), self.audio_file_path]
            print(f"Running command (Windows - ffplay): {' '.join(command)}")
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(self.duration)
            process.terminate()
        except :
            print("Couuld not play the audio.")
            

    def play_audio_mac(self):
        """Play audio on macOS using afplay."""
        command = ["afplay", self.audio_file_path]
        print(f"Running command (macOS): {' '.join(command)}")
        process = subprocess.Popen(command)
        process.wait()

    def play_audio_linux(self):
        """Play audio on Linux using ffplay."""
        command = ["ffplay", "-autoexit", "-nodisp", "-t", str(self.duration), self.audio_file_path]
        print(f"Running command (Linux): {' '.join(command)}")
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(self.duration)
        process.terminate()

    def play_audio(self):
        """Determine the OS, adjust duration, and play the audio accordingly."""
        self.adjust_duration()
        system = platform.system()
        print(f"Detected operating system: {system}")
        try:
            if system == "Windows":
                self.play_audio_windows()
            elif system == "Darwin":  # macOS
                self.play_audio_mac()
            else:
                # Assume Linux or other Unix-like OS
                self.play_audio_linux()
            print(f"Playback stopped after {self.duration} seconds.")
        except Exception :
            print("An error occurred while trying to play audio:")
    
