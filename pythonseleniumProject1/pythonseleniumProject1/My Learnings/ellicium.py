import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:


    def locate_by_id_demo(self):

        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.google.com/")
        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,"truncate").send_keys("tesla")
       # driver.find_element(By.XPATH,"//span[normalize-space()='News']").click()







findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
