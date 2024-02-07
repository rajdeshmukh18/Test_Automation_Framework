import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup_class(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    request.cls.driver = driver
    yield
    driver.close()
