import pytest
import softest
from selenium.webdriver.common.by import By
import time
from Test_Automation_Framework.pages.Search_Fligts_Results import Serach_Flight_result
from Test_Automation_Framework.pages.test_yatra_launch import LaunchPage
from Test_Automation_Framework.utilities.uti import Utilis


@pytest.mark.usefixtures("testsetup_class")
class TestDemoAutoSugg(softest.TestCase):
    def test_Demo_Auto_sugg(self):
        #Launch page
        lp=LaunchPage(self.driver)
        #called Depart From Location
        lp.enterDepartmentLocation("New Delhi")
        #Called Destination Location
        time.sleep(3)
        lp.enterGoingToLocation("Mumbai")
        #Selecting Date
        time.sleep(3)
        lp.enterDepartureDate("15/02/2024")
        #Searching Flights
        time.sleep(3)
        lp.clickSearchFlightButton()
        #Dynamic Scroll Bar
        time.sleep(2)
        lp.Page_Scroll()
        #FilterFlights
        time.sleep(3)
        sf=Serach_Flight_result(self.driver)
        sf. Filter_Condition("1 Stop")
        time.sleep(2)
        allstops1 = self.driver.find_elements(By.XPATH,"//span[contains(text(),'Non-Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")
        print(len(allstops1))
        time.sleep(2)
        time.sleep(1)
        ut=Utilis()
        ut.assertListItem(allstops1,"1 Stop")
        time.sleep(2)


