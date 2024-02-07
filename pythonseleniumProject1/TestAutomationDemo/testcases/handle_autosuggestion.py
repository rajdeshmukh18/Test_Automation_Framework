import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Handle_autosuggestion:
    def locate_by_id_demo(self):
        global lastCount
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        depart_form = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_form.click()
        time.sleep(2)
        inp = open("demo.txt", "r")
        depart_form.send_keys(inp)

        time.sleep(2)
        depart_form.send_keys(Keys.ENTER)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        going_to.send_keys("New York")
        time.sleep(2)
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for res in search_result:
            if "New York" in res.text:
                res.click()
                break
        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(2)
        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "30/01/2024":
                date.click()
                time.sleep(2)
                break


        time.sleep(4)
        driver.find_element(By.XPATH,
                            "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
        time.sleep(4)

        driver.close()


find_auto_sug = Handle_autosuggestion()
find_auto_sug.locate_by_id_demo()
