import logging
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
        Login_Test.run_test("Username Textbox Enable", True, unm.is_enabled())
        Login_Test.run_test("Password Textbox Enable", True, passw.is_enabled())
        Login_Test.run_test("Login Button Enable", True, lgnbut.is_enabled())
        lgnbut.click()
        Login_Test.run_test("Required msg displayed", True, driver.find_element(By.XPATH,
                                                                                "//div[@class='orangehrm-login-slot"
                                                                                "-wrapper']//div[1]//div[1]//span["
                                                                                "1]").text == "Required" and driver.find_element(
            By.XPATH, "//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]").text == "Required")
        unm.send_keys("A")
        lgnbut.click()
        Login_Test.run_test("Required msg displayed for password only", True, driver.find_element(By.XPATH,
                                                                                             "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
                            == "Required")

        driver.refresh()
        passw2=driver.find_element(By.NAME,"password")
        passw2.send_keys("A")
        lgnbut2=driver.find_element(By.TAG_NAME,"button")
        lgnbut2.click()

        Login_Test.run_test("Required msg displayed for username only", True, driver.find_element(By.XPATH,
                                                                                             "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
                            == "Required")
        driver.close()


login = Login_Test()
login.verify_cred()
