import os
from dotenv import load_dotenv

load_dotenv()

MEET_LINK = os.getenv("MEET_LINK")
AUDIO_FILE = os.getenv("AUDIO_FILE")
AUDIO_DURATION = int(os.getenv("AUDIO_DURATION"))
EMAIL = os.getenv("EMAIL_ID")
PASSWORD = os.getenv("EMAIL_PASSWORD")