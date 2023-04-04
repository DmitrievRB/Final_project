import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    s = Service('driver/chromedriver.exe')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=s, options=chrome_options)

    yield driver
    driver.quit()
