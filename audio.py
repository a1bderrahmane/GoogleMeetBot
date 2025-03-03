import time
from config import AUDIO_DURATION, JS_FILE, AUDIO_FILE
from pydub.playback import play
import subprocess


class Audio:
    def __init__(self, driver):
        self.driver = driver
        self.js_file_path = JS_FILE
        self.audio_file_path = "music.mp3"
        self.duration = AUDIO_DURATION
    def play_audio(self):
        
        subprocess.run(["ffplay", "-autoexit", "-nodisp", self.audio_file_path])## command for windows 
        ## add the command for linux
        time.sleep(self.duration)
        # Terminate the process if it's still running
        subprocess.terminate()
        print(f"Playback stopped after {self.duration} seconds.")

        # # Read the JavaScript file
        # with open(self.js_file_path, "r", encoding="utf-8") as file:
        #     js_script = file.read()

        # js_script = js_script.replace("{{AUDIO_SRC}}", AUDIO_FILE)

        # self.driver.execute_script(js_script)
        # print("\033[1;32mInjected JavaScript file and started playing audio!\033[0m")

        # time.sleep(AUDIO_DURATION)
