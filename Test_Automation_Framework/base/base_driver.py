import time

from selenium.webdriver.common.by import By


class BaseDriver:
    def __init__(self,driver):
        self.driver=driver
    def Page_Scroll(self):
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


