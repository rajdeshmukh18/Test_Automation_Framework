import time

from selenium.webdriver.common.by import By

from Test_Automation_Framework.base.base_driver import BaseDriver


class Serach_Flight_result(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    STOPS_1Filter= "//section[@id='Flight-APP']//label[2]"
    ALL_STOPS="//span[contains(text(),'Non-Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"
    def getFilter_flight(self):
        allstops = self.driver.find_elements(By.XPATH,self.ALL_STOPS)
        print(len(allstops))
        return self.driver.find_element(By.XPATH,self.STOPS_1Filter)

    def Filter_Condition(self,value):
        self.getFilter_flight().click()
        time.sleep(3)
