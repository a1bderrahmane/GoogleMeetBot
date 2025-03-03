from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from config import EMAIL, PASSWORD

class GoogleAuthenticator:
    def __init__(self):
        self.email = EMAIL
        self.password = PASSWORD
        options = Options()
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 0,
            "profile.default_content_setting_values.geolocation": 0
        })
        #  Disable pop-ups
        options.add_argument("--use-fake-ui-for-media-stream")  
        options.add_argument("--disable-features=WebRtcHideLocalIpsWithMdns")
        options.add_argument("--autoplay-policy=no-user-gesture-required")
        options.add_argument("--disable-features=PreloadMediaEngagementData,MediaEngagementBypassAutoplayPolicies")

        self.driver = webdriver.Chrome(options=options)

    
    def open_login_page(self):
        """Ouvre la page de connexion de Google."""
        self.driver.get("https://accounts.google.com/")

    def enter_email(self):
        """Saisit l'email et passe à l'étape suivante.
        
        Retourne True en cas de succès, False sinon.
        """
        try:
            email_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "identifierId"))
            )
            email_input.send_keys(self.email)
            self.driver.find_element(By.ID, "identifierNext").click()
            return True
        except TimeoutException:
            print("\033[1;31mErreur: Email input not found\033[0m")
            return False

    def wait_for_password_field(self):
        """Attend l'apparition du champ de saisie du mot de passe.
        
        Retourne l'élément si trouvé, sinon None.
        """
        try:
            password_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.NAME, "Passwd"))
            )
            return password_input
        except TimeoutException:
            return None

    def check_email_error(self):
        """Vérifie s'il y a un message d'erreur lié à l'email incorrect.
        
        Retourne True si une erreur est détectée, sinon False.
        """
        try:
            self.driver.find_element(By.XPATH, "//div[@jsname='B34EJ']")
            print("\033[1;31mErreur: Email incorrect\033[0m")
            return True
        except NoSuchElementException:
            return False

    def enter_password(self, password_input):
        """Saisit le mot de passe et soumet le formulaire.
        
        Retourne True en cas de succès, False sinon.
        """
        try:
            password_input.send_keys(self.password)
            self.driver.find_element(By.ID, "passwordNext").click()
            return True
        except Exception as e:
            print(f"\033[1;31mErreur during password input: \033[0m")
            return False

    def verify_login(self):
        """Vérifie si la connexion a réussi en attendant la présence d'un élément caractéristique.
        
        Retourne True si la connexion est validée, False sinon.
        """
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='GiKO7c']"))
            )
            print("Login successful!")
            return True
        except TimeoutException:
            try:
                self.driver.find_element(By.XPATH, "//div[@jsname='B34EJ']")
                print("\033[1;31mErreur: Mot de passe incorrect\033[0m")
            except NoSuchElementException:
                print("\033[1;31mErreur: Login process timed out\033[0m")
            return False

    def login(self):
        """Procède à l'ensemble du processus de connexion."""
        self.open_login_page()
        
        if not self.enter_email():
            self.driver.quit()
            return
        
        password_input = self.wait_for_password_field()
        if not password_input:
            if self.check_email_error():
                self.driver.quit()
                return
            else:
                print("\033[1;31mErreur: Timeout waiting for password field\033[0m")
                self.driver.quit()
                return

        if not self.enter_password(password_input):
            self.driver.quit()
            return

        if not self.verify_login():
            self.driver.quit()
            return

        return self.driver
    
