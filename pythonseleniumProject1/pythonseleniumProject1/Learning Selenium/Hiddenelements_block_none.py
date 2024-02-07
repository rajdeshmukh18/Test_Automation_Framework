import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
'''class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        x = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(x)
        driver.find_element(By.XPATH, "//button[@class='ws-btn w3-hover-black w3-dark-grey']").click()
        y = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(y)
        time.sleep(2)
   '''


class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        driver.get("https://www.yatra.com/hotels")
        driver.fullscreen_window()
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()

        driver.find_element(By.XPATH,
                            "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        x = driver.find_element(By.XPATH,
"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").is_displayed()
        print(x)
        time.sleep(10)


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
