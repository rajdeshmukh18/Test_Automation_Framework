import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.find_element(By.PARTIAL_LINK_TEXT,'Yatra for Business').click()
        time.sleep(5)


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
