import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="https://google.com/")

@pytest.fixture()
def setup(pytestconfig):
    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
    # s = Service(r"C:\Users\AAIC\Downloads\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Chrome(service=s)
    if pytestconfig.getoption("browser").lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        chromedriver_path =Service(r"/usr/local/bin/chromedriver")
        # s = Service(r"C:\Users\AAIC\Downloads\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service= chromedriver_path,options=options)
        driver.maximize_window()

    elif pytestconfig.getoption("browser").lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver_path =r"/usr/bin/geckodriver"
        # driver_path =Service(r"C:\Users\AAIC\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe")
        driver = webdriver.Firefox(executable_path=driver_path,options=options)
        driver.maximize_window()

    yield {"driver": driver, "url": pytestconfig.getoption("url")}
    


@pytest.fixture(scope='session')
def timings(metadata):
    """
    used to calculate Analytics
    """
    Analytics = {}

    def factory(response_time):
        response_time = response_time/1000000
        throughput = 60/(1 + response_time)
        # fsw = {'response_time': response_time,"throughput":throughput}
        Analytics["Response_time"] = response_time
        Analytics["Throughput"] = throughput
        

    yield factory

    # add our Analytics to the json_report metadata so that we can report it out
    metadata['Analytics'] = Analytics



# @pytest.hookimpl(optionalhook=True)
# def pytest_json_modifyreport(json_report):
#     Analytics = json_report['environment']['Analytics']
