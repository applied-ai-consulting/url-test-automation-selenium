import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://google.com/")

@pytest.fixture()
def setup(pytestconfig):
    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
    # s = Service(r"C:\Users\AAIC\Downloads\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Chrome(service=s)
    options = webdriver.ChromeOptions()
    chrome_path = Service("/usr/local/bin/chromedriver")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(service=chrome_path,options=options)
    driver.maximize_window()
    yield {"driver": driver, "url": pytestconfig.getoption("url")}