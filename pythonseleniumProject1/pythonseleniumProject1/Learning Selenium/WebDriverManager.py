from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Automatically download and use the latest ChromeDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_title():
     # Navigate to the website
    driver.get("https://www.google.com")

    # Get the title of the page
    title = driver.title

    # Verify the title
    expected_title = "Google"
    if title == expected_title:
        print("Title verification successful!")
    else:
        print(f"Title verification failed. Expected '{expected_title}', but got '{title}'.")

    # Close the browser
    driver.quit()


if __name__ == "__main__":
    verify_title()