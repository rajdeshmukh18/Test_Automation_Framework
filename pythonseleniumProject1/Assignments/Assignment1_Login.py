import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
class TerminalColors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

class Login_Test:
    @staticmethod
    def run_test(test_name, actual, expected):
        try:
            assert actual == expected
            print(f"{TerminalColors.GREEN}Test passed: {test_name}{TerminalColors.RESET}")
        except AssertionError as e:
            logging.error(f"{TerminalColors.RED}Test failed: {test_name}. {e}" + f"Actual: {actual}  " + f"Expected:{expected}{TerminalColors.RESET}")
        return actual == expected

    def verify_cred(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(5)
        driver.maximize_window()
        unm = driver.find_element(By.NAME, "username")
        passw = driver.find_element(By.NAME, "password")
        lgnbut = driver.find_element(By.TAG_NAME, "button")
        if Login_Test.run_test("Username Textbox Enabled", True, unm.is_enabled()):
            unm.get_attribute("Admin")
            time.sleep(3)
        if Login_Test.run_test("Password Textbox Enabled", True, passw.is_enabled()):
            passw.send_keys("admin123")
            time.sleep(3)
        if Login_Test.run_test("Login Button Enabled", True, lgnbut.is_enabled()):
            lgnbut.click()
            Login_Test.run_test("User redirected to Home Page", True,
                                driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php"
                                                      "/dashboard/index")
        driver.close()


login = Login_Test()
login.verify_cred()