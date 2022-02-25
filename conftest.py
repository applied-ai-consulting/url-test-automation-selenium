import pytest
from pytz import timezone
from datetime import datetime 
from selenium import webdriver


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
    chromedriver_path ="/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(chromedriver_path,chrome_options=chrome_options)
    driver.maximize_window()
    yield {"driver": driver, "url": pytestconfig.getoption("url")}


@pytest.hookimpl(optionalhook=True)
def pytest_json_runtest_metadata(call):
    """
    fixture from the pytest-json-report plugin that will add your info
    """
    if call.when != 'call':
       return {}

    # collect the start and finish times in ISO format for the US/Eastern timezone
    start_iso_dt = timezone('Asia/Kolkata').localize(datetime.fromtimestamp(call.start))
    stop_iso_dt = timezone('Asia/Kolkata').localize(datetime.fromtimestamp(call.stop))
    response_time = (stop_iso_dt - start_iso_dt).total_seconds()
    throughput = 60/(1 + response_time)
    return {'response_time': str(response_time),"throughput" : str(throughput/60)}
