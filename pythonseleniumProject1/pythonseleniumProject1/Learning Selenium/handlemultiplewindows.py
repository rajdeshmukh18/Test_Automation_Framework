import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class FindElementByCssSelector:
    def locate_by_id_demo(self):
        global all_handles2
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle=driver.current_window_handle
        print(parent_handle)
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@title='Claim Refund']//img[@class='conta iner large-banner']").click()
        all_handles=driver.window_handles
        print(all_handles)
        time.sleep(2)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                second=driver.current_window_handle
                print(second)
                driver.find_element(By.XPATH, "//a[normalize-space()='customer care']").click()
                time.sleep(2)
                all_handles2 = driver.window_handles
                print(all_handles2)
                time.sleep(3)
                for hand in all_handles2:
                    if parent_handle!=hand and second!=hand:
                        driver.switch_to.window(hand)
                        driver.find_element(By.XPATH,"//input[@id='req']").send_keys("Hello")
                        time.sleep(2)
                        driver.close()
                        break
                driver.switch_to.window(second)
                driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys("Hello")
                time.sleep(2)
                driver.close()
                break
        driver.switch_to.window(parent_handle)
        time.sleep(2)
        driver.close()

        
findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
