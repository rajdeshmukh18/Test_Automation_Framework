import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCssSelector:


    def locate_by_id_demo(self):
        global all_handles2, child
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.w3schools.com/")
        time.sleep(2)
        parent = driver.current_window_handle
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@class='user-anonymous tnb-certificates-btn w3-bar-item w3-button w3-right w3-white ga-top ga-top-certificates']").click()
        time.sleep(2)
        if len(driver.window_handles)> 1:
            print("More than 1 screens :"+str(len(driver.window_handles)))
            print(driver.window_handles)
            for i in driver.window_handles:
                if i!=parent:
                    child=i
                    driver.switch_to.window(i)
            print("User switched to this window URL:" + str(driver.current_url))
            time.sleep(2)
            driver.switch_to.window(parent)
            time.sleep(2)
            driver.switch_to.window(child)
            driver.close()




findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
