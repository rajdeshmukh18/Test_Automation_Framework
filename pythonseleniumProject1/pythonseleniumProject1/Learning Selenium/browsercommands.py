import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        driver.minimize_window()
        time.sleep(2)
        driver.quit()


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
