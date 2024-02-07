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
            logging.error(
                f"{TerminalColors.RED}Test failed: {test_name}. {e}" + f"Actual: {actual}  " + f"Expected:{expected}{TerminalColors.RESET}")
        return actual == expected

    def verify_cred(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(5)
        driver.maximize_window()
        unm = driver.find_element(By.NAME, "username")
        passw = driver.find_element(By.NAME, "password")
        lgnbut = driver.find_element(By.TAG_NAME, "button")
        if Login_Test.run_test("Username Textbox Enable", True, unm.is_enabled()):
            unm.send_keys("Admin")
        if Login_Test.run_test("Password Textbox Enable", True, passw.is_enabled()):
            passw.send_keys("admin12")
        if Login_Test.run_test("Login Button Enable", True, lgnbut.is_enabled()):
            lgnbut.click()
            Login_Test.run_test("Error Message Displayed for invalid password", True, driver.find_element(By.XPATH,
                                                                                                          "//p[@class='oxd-text "
                                                                                                          "oxd-text--p "
                                                                                                          "oxd-alert-content-text']").text
                                == "Invalid credentials")


login = Login_Test()
login.verify_cred()
