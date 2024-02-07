import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:


    def locate_by_id_demo(self):
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        achains = ActionChains(driver)
       # singlerightclick=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
       # achains.context_click(singlerightclick).perform()
        #time.sleep(2)
        ele2=driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(ele2).perform()
        driver.switch_to.alert.accept()
        time.sleep(2)


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
