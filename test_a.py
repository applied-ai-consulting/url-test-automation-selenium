from datetime import datetime
import pytest
import time

@pytest.mark.usefixtures("timings")
def test_Openurl(setup,timings):

    driver = setup["driver"]
    url = setup["url"]
    if not url.endswith('/'):
        url = url + '/'
    before_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
    driver.get(url)
    driver.set_page_load_timeout(240)    
    now_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
    response_time = int(now_time) - int(before_time)
    print(response_time)
    first_url_response_time = timings(response_time)
    stripped_url = url.replace("https://", "").replace("http://", "")
    assert stripped_url in driver.current_url
    # assert driver.current_url == url
    time.sleep(15)
    driver.save_screenshot("report/ss.png")
    print('assertion passed')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(15)
    driver.save_screenshot("report/ss1.png")
    driver.close()
