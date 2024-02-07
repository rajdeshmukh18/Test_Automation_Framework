import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        x = driver.find_element(By.NAME, "UserTitle")
        dd=Select(x)
        dd.select_by_index(4)
        time.sleep(2)
        dd.select_by_visible_text("Marketing / PR Manager")
        time.sleep(2)



findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
