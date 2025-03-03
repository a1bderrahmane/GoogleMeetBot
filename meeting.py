from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from audio import Audio

class GoogleMeetBot:
    def __init__(self, driver, meet_link):
        self.driver = driver
        self.meet_link = meet_link
        self.meeting_id = meet_link.split("/")[-1]

    def join_meeting(self):
        self.driver.get(self.meet_link)
        # Click on the join meeting button
        try:
            join_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(@class, 'UywwFc-RLmnJb')]/parent::button")
                )
            )
            join_button.click()
            print("\033[1;32mClicked 'Participer' (Join) button!\033[0m")
        except Exception as e:
            print(f"\033[1;31mErreur: Couldn't click 'Participer'. {e}\033[0m")
            self.driver.quit()
            return

        # Check if the meeting has started by detecting the meeting ID div
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[@data-meeting-title='{self.meeting_id}']")
                )
            )
            print(f"\033[1;34mSuccessfully joined the meeting! (Meeting ID: {self.meeting_id} detected)\033[0m")
        except Exception as e:
            print(f"\033[1;31mErreur: Meeting ID div not found. You may not have joined successfully. {e}\033[0m")
            self.driver.quit()
            return

        # Play audio using the Audio class
        audio = Audio(self.driver)
        audio.play_audio()

        # Stay in the meeting indefinitely
        print("Staying in the meeting. Press CTRL+C to exit.")
        try:
            while True:
                time.sleep(30)  # Keeps the session alive; adjust as needed.
        except KeyboardInterrupt:
            print("Exiting the meeting...")
            self.driver.quit()

    def leave_meeting(self):
        self.driver.quit()
