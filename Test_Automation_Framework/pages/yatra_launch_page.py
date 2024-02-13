import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class Launch_Page:
    def __init__(self, driver,wait):
        self.driver = driver
        self.wait=wait

    def departfrom(self, departloc):
        depart = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart.click()
        time.sleep(2)
        depart.send_keys(departloc)
        time.sleep(2)
        depart.send_keys(Keys.ENTER)
        time.sleep(2)

    def goingto(self, goingtoloc):
        arr = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(2)
        arr.send_keys(goingtoloc)
        time.sleep(2)

        search_result = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for res in search_result:
            if "New York" in res.text:
                res.click()
                time.sleep(2)
                break

    def selectdate(self, depdate):
        da = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        da.click()
        time.sleep(2)
        all_date = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveID']")

        for date in all_date:
            if date.get_attribute("data-date") == depdate:
                date.click()
                time.sleep(2)
                break
        time.sleep(3)

    def clicksearch(self):
        self.driver.find_element(By.XPATH,
                                 "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()
