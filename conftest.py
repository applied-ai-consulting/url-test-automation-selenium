import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://google.com/")

@pytest.fixture()
def setup(pytestconfig):
    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
    # s = Service(r"C:\Users\AAIC\Downloads\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Chrome(service=s)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield {"driver": driver, "url": pytestconfig.getoption("url")}