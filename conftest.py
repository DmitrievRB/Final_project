import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    s = Service('driver/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")

    yield driver
    driver.quit()
