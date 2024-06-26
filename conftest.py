import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.safari.options import Options as SafariOptions
# from selenium.webdriver.chrome.service import Service
from func_firefox import firefox_webdrvr


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="safari")
    parser.addoption("--url", action="store", default="https://google.com/")

@pytest.fixture()
def setup(pytestconfig):
    # chrome_options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(ChromeDriverManager().download_and_install())
    # s = Service(r"C:\Users\AAIC\Downloads\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Chrome(service=s)
    if pytestconfig.getoption("browser_name").lower() == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        chromedriver_path =Service(r"/usr/local/bin/chromedriver")
        #driver_path = ChromeDriverManager().install()

        # driver = webdriver.Chrome(executable_path=chromedriver_path,options=options)
        driver = webdriver.Chrome(service = chromedriver_path,options=options)
        driver.maximize_window()

    elif pytestconfig.getoption("browser_name").lower() == "firefox":
        driver = firefox_webdrvr()
        driver.maximize_window()

    elif pytestconfig.getoption("browser_name").lower() == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        edgedriver_path =Service(r"/usr/local/bin/msedgedriver")
        # edgedriver_path1=webdriver.Edge(EdgeChromiumDriverManager().install())

        # s = Service(r"C:\Users\AAIC\Downloads\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Edge(service= edgedriver_path,options=options)
        driver.maximize_window()
        
    elif pytestconfig.getoption("browser_name").lower() == "safari":
        options = SafariOptions()
        options.add_argument("--headless")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # driver = webdriver.Safari(options=options)
        driver = webdriver.Safari(executable_path='/usr/bin/WebKitWebDriver', options=options)
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
        print(f"response_time:{response_time}")
        print(f"throughput:{throughput}")
        

    yield factory

    # add our Analytics to the json_report metadata so that we can report it out
    metadata['Analytics'] = Analytics



# @pytest.hookimpl(optionalhook=True)
# def pytest_json_modifyreport(json_report):
#     Analytics = json_report['environment']['Analytics']
