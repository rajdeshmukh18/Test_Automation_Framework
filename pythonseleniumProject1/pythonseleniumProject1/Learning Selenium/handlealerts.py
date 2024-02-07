import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:


    def locate_by_id_demo(self):
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame("iframeResult")

        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        driver.switch_to.alert.send_keys("Raj Deshmukh")
        driver.switch_to.alert.accept()
        time.sleep(2)

    ''''driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)
'''
findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
