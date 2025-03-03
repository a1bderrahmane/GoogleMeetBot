from authentication import GoogleAuthenticator
from meeting import GoogleMeetBot
from config import MEET_LINK
import os
import sys
sys.tracebacklimit = 0

def main():
    os.environ['TMP'] = "D:\Temp"
    os.environ['TEMP'] = "D:\Temp"
    auth = GoogleAuthenticator()
    driver = auth.login()
    if(driver==None):
        print("Erreur lors de la connexion")
        return 
    bot = GoogleMeetBot(driver, MEET_LINK)
    bot.join_meeting()

if __name__ == "__main__":
    main()

