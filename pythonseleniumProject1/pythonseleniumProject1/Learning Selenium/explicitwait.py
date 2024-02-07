import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Handleautosuggestion:
    def locate_by_id_demo(self):
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.yatra.com/")
        driver.fullscreen_window()
        depart_form = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_form.click()
        time.sleep(2)
        inp = open("demo.txt", "r")
        depart_form.send_keys(inp)

        time.sleep(2)
        depart_form.send_keys(Keys.ENTER)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        going_to.send_keys("Mumbai")
        time.sleep(2)
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for res in search_result:
            if "Mumbai" in res.text:
                res.click()
                break
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()

        all_dates = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                                              "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))).find_elements(
            By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "30/01/2024":
                date.click()
                break
        driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()

findautosug = Handleautosuggestion()
findautosug.locate_by_id_demo()
