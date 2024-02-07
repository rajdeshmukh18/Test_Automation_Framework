import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("setup_class")
class TestAutoSugg():
    def test_auto_suggest(self):
        depart = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart.click()
        time.sleep(2)
        depart.send_keys("New Delhi")
        time.sleep(2)
        depart.send_keys(Keys.ENTER)
        time.sleep(2)

        arr = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        arr.send_keys("Mum")
        time.sleep(2)

        search_result = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for res in search_result:
            if "Mumbai" in res.text:
                res.click()
                time.sleep(2)
                break
        da = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        da.click()
        time.sleep(2)
        all_date = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveID']")

        for date in all_date:
            if date.get_attribute("data-date") == "22/01/2024":
                date.click()
                time.sleep(2)
                break
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
        time.sleep(2)
        # Dynamic Scroll Bar
        pageLength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight;")
            if lastCount == pageLength:
                match = True
        time.sleep(4)

        allstops = self.driver.find_elements(By.XPATH,
                                             "//span[contains(text(),'Non-Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        print(len(allstops))
        self.driver.find_element(By.XPATH, "//section[@id='Flight-APP']//label[2]").click()
        time.sleep(2)
        allstops1 = self.driver.find_elements(By.XPATH,
                                              "//span[contains(text(),'Non-Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        print(len(allstops1))
        for stop in allstops1:
            print("The text is:" + stop.text)
            assert stop.text == "1 Stop"
            print("assert pass")
        time.sleep(4)


