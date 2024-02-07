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
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        morebutton=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        achains=ActionChains(driver)
        achains.move_to_element(morebutton).perform()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@id='booking_engine_xplore']").click()
        time.sleep(2)

findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
