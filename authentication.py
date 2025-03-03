from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()

class GoogleAuthenticator:
    def __init__(self):
        self.email = os.getenv("EMAIL_ID")
        self.password = os.getenv("EMAIL_PASSWORD")
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1
        })
        # ✅ Disable pop-ups
        options.add_argument("--use-fake-ui-for-media-stream")  
        options.add_argument("--disable-features=WebRtcHideLocalIpsWithMdns")
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies")

        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://accounts.google.com/")

        # Enter email and click next
        try:
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )
            email_input.send_keys(self.email)
            self.driver.find_element(By.ID, "identifierNext").click()
        except TimeoutException:
            print("\033[1;31mErreur: Email input not found\033[0m")
            self.driver.quit()
            return

        # Wait for the password field or email error message
        try:
            # Wait until the password field is present
            password_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "Passwd"))
            )
        except TimeoutException:
            # Try to capture an error message indicating the email is wrong
            try:
                error_element = self.driver.find_element(By.XPATH, "//div[@jsname='B34EJ']")
                print("\033[1;31mErreur: Email incorrect\033[0m")
            except NoSuchElementException:
                print("\033[1;31mErreur: Timeout waiting for password field\033[0m")
            self.driver.quit()
            return

        # Enter password and click next
        try:
            password_input.send_keys(self.password)
            self.driver.find_element(By.ID, "passwordNext").click()
        except Exception as e:
            print(f"\033[1;31mErreur during password input: {e}\033[0m")
            self.driver.quit()
            return

        # Wait for an element that indicates successful login or a password error message
        try:
            # Replace the below locator with an element that is unique to the account page after login
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='GiKO7c']"))
            )
            print("Login successful!")
        except TimeoutException:
            try:
                # Check if there's a password error message displayed
                error_element = self.driver.find_element(By.XPATH,"//div[@jsname='B34EJ']")
                print("\033[1;31mErreur: Mot de passe incorrect\033[0m")
            except NoSuchElementException:
                print("\033[1;31mErreur: Login process timed out\033[0m")
            self.driver.quit()
            return

        return self.driver
