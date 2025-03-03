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

    def open_meet_link(self):
        """Ouvre le lien de la réunion."""
        self.driver.get(self.meet_link)

    def validate_meet_link(self):
        """
        Valide le lien de la réunion en vérifiant la présence du bouton 'Participer'.
        Retourne True si le bouton est détecté, sinon affiche une erreur et retourne False.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//span[contains(@class, 'UywwFc-RLmnJb')]/parent::button")
                )
            )
            return True
        except Exception as e:
            print(f"\033[1;31mErreur: Le lien de réunion semble incorrect car le bouton 'Participer' n'a pas été trouvé. \033[0m")
            return False

    def click_join_button(self):
        """Clique sur le bouton 'Participer' (Join)."""
        try:
            join_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//span[contains(@class, 'UywwFc-RLmnJb')]/parent::button")
                )
            )
            join_button.click()
            print("\033[1;32mClicked 'Participer' (Join) button!\033[0m")
            return True
        except Exception as e:
            print(f"\033[1;31mErreur: Couldn't click 'Participer'. \033[0m")
            return False

    def verify_meeting_started(self):
        """Vérifie si la réunion a démarré en détectant la présence de l'élément identifiant la réunion."""
        try:
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//div[@data-meeting-title='{self.meeting_id}']")
                )
            )
            print(f"\033[1;34mSuccessfully joined the meeting! (Meeting ID: {self.meeting_id} detected)\033[0m")
            return True
        except Exception as e:
            print(f"\033[1;31mErreur: Meeting ID div not found. You may not have joined successfully.\033[0m")
            return False

    def play_audio(self):
        """Joue l'audio en utilisant la classe Audio."""
        audio = Audio(self.driver)
        audio.play_audio()

    def maintain_meeting(self):
        """Maintient la session dans la réunion jusqu'à interruption par l'utilisateur."""
        print("Staying in the meeting. Press CTRL+C to exit.")
        try:
            while True:
                time.sleep(30)  # Garde la session active ; ajuster selon les besoins.
        except KeyboardInterrupt:
            print("Exiting the meeting...")
            self.driver.quit()

    def join_meeting(self):
        """Orchestre le processus complet pour rejoindre la réunion et jouer le fichier audio."""
        self.open_meet_link()

        # Vérifie si le lien de réunion est correct via la présence du bouton 'Participer'
        if not self.validate_meet_link():
            self.driver.quit()
            return

        if not self.click_join_button():
            self.driver.quit()
            return

        if not self.verify_meeting_started():
            self.driver.quit()
            return

        self.play_audio()
        # self.maintain_meeting()

    def leave_meeting(self):
        """Quitte la réunion."""
        self.driver.quit()


    # def join_meeting(self):
    #     self.driver.get(self.meet_link)
    #     # Click on the join meeting button
    #     try:
    #         join_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable(
    #                 (By.XPATH, "//span[contains(@class, 'UywwFc-RLmnJb')]/parent::button")
    #             )
    #         )
    #         join_button.click()
    #         print("\033[1;32mClicked 'Participer' (Join) button!\033[0m")
    #     except Exception as e:
    #         print(f"\033[1;31mErreur: Couldn't click 'Participer'. \033[0m")
    #         self.driver.quit()
    #         return

    #     # Check if the meeting has started by detecting the meeting ID div
    #     try:
    #         WebDriverWait(self.driver, 15).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, f"//div[@data-meeting-title='{self.meeting_id}']")
    #             )
    #         )
    #         print(f"\033[1;34mSuccessfully joined the meeting! (Meeting ID: {self.meeting_id} detected)\033[0m")
    #     except Exception as e:
    #         print(f"\033[1;31mErreur: Meeting ID div not found. You may not have joined successfully. \033[0m")
    #         self.driver.quit()
    #         return

    #     # Play audio using the Audio class
    #     audio = Audio(self.driver)
    #     audio.play_audio()

    #     # Stay in the meeting indefinitely
    #     print("Staying in the meeting. Press CTRL+C to exit.")
    #     try:
    #         while True:
    #             time.sleep(30)  # Keeps the session alive; adjust as needed.
    #     except KeyboardInterrupt:
    #         print("Exiting the meeting...")
    #         self.driver.quit()

    # def leave_meeting(self):
    #     self.driver.quit()
