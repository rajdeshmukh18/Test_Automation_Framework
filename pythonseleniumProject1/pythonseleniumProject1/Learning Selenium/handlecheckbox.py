from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoCheckbox():
    def Demo_check_box(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.fullscreen_window()
        driver.get("https://www.yatra.com/flights")

        driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").click()
        time.sleep(3)
        var=driver.find_element(By.XPATH,"(//i[@class='ico ico-checkbox'])[2]").get_attribute("class")
        print(var)
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[normalize-space()='Student Fare']").click()
        time.sleep(3)
        var1=driver.find_element(By.XPATH,"//a[normalize-space()='Student Fare']").is_selected()
        print(var1)
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").click()
        time.sleep(3)
        var2 = driver.find_element(By.XPATH, "//a[normalize-space()='Non Stop Flights']").is_selected()
        print(var2)
        driver.close()
che=DemoCheckbox()
che.Demo_check_box()
