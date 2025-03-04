from authentication import GoogleAuthenticator
from meeting import GoogleMeetBot
from config import MEET_LINK
import sys

sys.tracebacklimit = 0

def main():
    auth = GoogleAuthenticator()
    driver = auth.login()
    if(driver==None):
        print("Erreur lors de la connexion")
        return 
    bot = GoogleMeetBot(driver, MEET_LINK)
    bot.join_meeting()
    bot.leave_meeting()

if __name__ == "__main__":
    main()

