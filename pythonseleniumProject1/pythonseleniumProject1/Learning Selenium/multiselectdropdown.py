import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class FindElementByCssSelector:
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")

        # Switch to the iframe
        iframe = driver.find_element(By.ID, "iframeResult")
        driver.switch_to.frame(iframe)

        # Now you can interact with elements inside the iframe
        dropdown = driver.find_element(By.NAME, "cars")
        dd = Select(dropdown)
        dd.select_by_index(0)
        dd.select_by_visible_text("Audi")
        time.sleep(2)

        # Switch back to the default content
        driver.switch_to.default_content()

findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
