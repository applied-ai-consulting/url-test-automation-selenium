from datetime import datetime


def test_Openurl(setup):

    driver = setup["driver"]
    url = setup["url"]
    url = url + "/"
    before_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
    driver.get(url)
    now_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
    response_time = int(now_time) - int(before_time)
    assert driver.current_url == url
    driver.save_screenshot("report/ss.png")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot("report/ss1.png")
    driver.close()
