from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.by import By


# Replace 'your_url' with the actual URL you want to scrape
class FindElementByCssSelector:

    def locate_by_id_demo(self):
        url_to_scrape = ('https://www.google.com/search?sca_esv=600971176&rlz=1C1OPNX_enIN1091IN1091&sxsrf=ACQVn0'
                         '-KkKUFh1vw9U9njlVJLP6poINFmA:1706071394252&q=tesla&tbm=nws&source=lnms&sa=X&ved'
                         '=2ahUKEwiyv6mbm_WDAxWJZvUHHaUWBY8Q0pQJegQIFRAB&biw=1280&bih=593&dpr=1.5')
        # Initialize a WebDriver (assuming ChromeDriver is installed)
        chrome_service = webdriver.chrome.service.Service(executable_path="C:\\browserdrivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_service)
        # Load the URL into the WebDriver
        driver.get(url_to_scrape)

        # Wait for a while to ensure the content is fully loaded
        driver.implicitly_wait(10)

        # Extract information
        try:
            # Extracting Fortune
            fortune_element = driver.find_element(By.CSS_SELECTOR,'.nejPhd')
            fortune_text = fortune_element.text.strip() if fortune_element else 'Fortune information not available'

            # Extracting the URL
            url_element = driver.find_element(By.CSS_SELECTOR,'.wlydoe')
            url = url_element.get_attribute('href') if url_element else 'URL not available'

            # Extracting time (15 hours ago)
            time_element = driver.find_element(By.CSS_SELECTOR,'.0SrXXb span')
            time_ago = time_element.text.strip() if time_element else 'Time information not available'

            # Printing the extracted information
            print(f"Fortune: {fortune_text}")
            print(f"URL: {url}")
            print(f"Time: {time_ago}")
        except Exception as e:
            print(f"Error: {e}")
        driver.quit()


findbycssselector = FindElementByCssSelector()
findbycssselector.locate_by_id_demo()
