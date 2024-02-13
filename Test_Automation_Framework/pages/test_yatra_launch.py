import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Test_Automation_Framework.base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    DEPART_FROM_FIELD= "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD="//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULT= "//div[@class='viewport']//div[1]/li"
    SELECT_DATES="//input[@id='BE_flight_origin_date']"
    ALL_DATES="//div[@id='monthWrapper']//tbody//td[@class!='inActiveID']"
    SEARCH_BUTTON="//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"
    def getDepartFromField(self):
        return self.driver.find_element(By.XPATH,self.DEPART_FROM_FIELD)

    def getGoingToLocation(self):
        return self.driver.find_element(By.XPATH,self.GOING_TO_FIELD)

    def getGoingToResult(self):
        return self.driver.find_elements(By.XPATH,self.GOING_TO_RESULT)

    def getDepartureDate(self):
        return self.driver.find_element(By.XPATH,self.SELECT_DATES)

    def getALLDatesField(self):
        return  self.driver.find_element(By.XPATH,self.ALL_DATES)

    def Search_Button(self):
        return self.driver.find_element(By.XPATH,self.SEARCH_BUTTON)

    def enterDepartmentLocation(self,departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        time.sleep(2)
        self.getDepartFromField().send_keys(Keys.ENTER)

    def enterGoingToLocation(self,destinationlocation):
        self.getGoingToLocation().click()
        self.getGoingToLocation().send_keys(destinationlocation)
        search_result = self.getGoingToResult()
        print(len(search_result))
        for res in search_result:
            if destinationlocation in res.text:
                res.click()
                time.sleep(2)
                break

    def enterDepartureDate(self,deptauredate):
        self.getDepartureDate().click()
        time.sleep(2)
        all_date = self.getALLDatesField().find_elements(By.XPATH,self.ALL_DATES)
        for date in all_date:
            if date.get_attribute("data-date") == deptauredate:
                date.click()
                time.sleep(2)
                break

    def clickSearchFlightButton(self):
        self.Search_Button().click()
        time.sleep(4)
