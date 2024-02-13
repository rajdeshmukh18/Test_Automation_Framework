import pytest
from selenium import webdriver
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="class")
def testsetup_class(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver=driver
    request.cls.wait=wait
    yield
    driver.close()
