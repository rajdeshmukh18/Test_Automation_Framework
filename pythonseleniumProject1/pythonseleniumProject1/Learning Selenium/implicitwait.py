import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Implicitwait:
    def imp_wait(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys('raj@ness.com')
        driver.find_element(By.XPATH, "// input[ @ id = 'passwor']").send_keys('raj@ness.com')


impwait = Implicitwait()
impwait.imp_wait()
