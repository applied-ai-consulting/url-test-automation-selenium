import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


# from selenium.webdriver.firefox.service import Service

def firefox_webdrvr():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    # driver_path = Service(r"/usr/bin/geckodriver")
    ff_driver_path = GeckoDriverManager().install()
    # driver_path =Service(r"C:\Users\AAIC\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe")
    driver = webdriver.Firefox(executable_path=ff_driver_path,options = options)
    return driver
