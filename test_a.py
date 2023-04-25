from datetime import datetime
import pytest

@pytest.mark.usefixtures("timings")
def test_Openurl(setup,timings):

    driver = setup["driver"]
    url = setup["url"]
    if not url.endswith('/'):
        url = url + '/'
    before_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
    driver.get(url)
    now_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
    response_time = int(now_time) - int(before_time)
    print(response_time)
    first_url_response_time = timings(response_time)
    assert driver.current_url == url
    driver.save_screenshot("report/ss.png")
    print('assertion passed')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot("report/ss1.png")
    driver.close()
