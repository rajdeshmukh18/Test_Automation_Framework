import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:


    def locate_by_id_demo(self):
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH,"//a[@title='Sign Up to Improve Your Learning Experience']").click()
        time.sleep(2)


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
