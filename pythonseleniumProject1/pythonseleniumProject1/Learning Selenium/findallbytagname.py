import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        list_a=driver.find_elements(By.TAG_NAME,'a')
        for i in list_a:
            print(i.text)
        print(len(list_a))
        time.sleep(5)


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
