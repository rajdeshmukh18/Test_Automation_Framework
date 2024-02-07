import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://training.openspan.com/login")
        x = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(x)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("raj@ness.com")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("raj@ness.com")
        y = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(y)


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
