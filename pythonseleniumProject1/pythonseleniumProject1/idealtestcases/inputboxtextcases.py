from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
class TerminalColors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
# Create a new instance of the Chrome driver
chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

# Open the HTML test page
driver.get(
    "file:///C:/python-selenium/pythonseleniumProject1/idealtestcases/testpage.html?_ijt=oppg6pefnik324u85c9pch00qo&_ij_reload=RELOAD_ON_SAVE")

# Find the textbox element by its ID
textbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'textbox')))
time.sleep(3)

#Common function for all
def run_test(test_name, actual, expected):
    try:
        assert actual == expected
        print(f"{TerminalColors.GREEN}{test_name}: Pass{TerminalColors.RESET}")
    except AssertionError as e:
        print(f"{TerminalColors.RED}{test_name}: Fail " + f"Actual Result: {actual}  " + f"Expected Result:{expected}{TerminalColors.RESET} ")

#Test Case 1
content = driver.find_element(By.XPATH, '//button[text()="Get Textbox Value"]').get_attribute("value")
if content == "":
    run_test("Before input disabled button",driver.find_element(By.XPATH, '//button[text()="Get Textbox Value"]').is_enabled(),False)
    textbox.send_keys("Hi")
    content=driver.find_element(By.XPATH, '//button[text()="Get Textbox Value"]').get_attribute("value")
    run_test("After input enabled button", driver.find_element(By.XPATH, '//button[text()="Get Textbox Value"]').is_enabled(), True)
else:
    run_test("After input", driver.find_element(By.XPATH, '//button[text()="Get Textbox Value"]').is_enabled(), False)

#Test Case 2
textbox.send_keys("Test Input@ness.com")
time.sleep(2)
run_test("Basic Input", textbox.get_attribute("value"), "Test Input")
time.sleep(2)


#Test Case 3
run_test("Contains @ness.com", textbox.get_attribute("value").__contains__("@ness.com"), True)
textbox.clear()
time.sleep(2)


#Test Case 4
run_test("TestInput", textbox.get_attribute("value"), "Test Input")


# Test Case 5: Special Characters
textbox.send_keys("!@#$%^&*(")
run_test("Special Characters", textbox.get_attribute("value"), "!@#$%^&*()")
time.sleep(2)


# Test Case 6: Numeric Input
textbox.clear()
textbox.send_keys("12345")
run_test("Numeric Input", textbox.get_attribute("value"), "12345")
time.sleep(2)


# Test Case 7: Clear Input
textbox.clear()
run_test("Clear Input", textbox.get_attribute("value"), "")
time.sleep(2)


# Test Case 8: Input Events
textbox.clear()
textbox.send_keys("Testing Input Events")
time.sleep(2)


button = driver.find_element(By.XPATH, '//button[text()="Get Textbox Value"]')
button.click()

driver.quit()
