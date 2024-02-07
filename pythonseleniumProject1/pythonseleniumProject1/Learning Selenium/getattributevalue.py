import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        x=driver.find_element(By.XPATH, "//input[@id='login-input']").get_attribute("type")
        print(x)



findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
