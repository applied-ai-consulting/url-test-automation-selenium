from datetime import datetime

def test_Openurl(setup):
    driver = setup["driver"]
    url = setup["url"]
    # import pdb
    # pdb.set_trace()
    try:
        before_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
        print(before_time)
        driver.get(url)
        now_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
        print(now_time)
    except Exception as e:
        print(e.message)
    # import pdb
    # pdb.set_trace()
    assert driver.current_url == url
    driver.save_screenshot("ss.png")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot("ss1.png")
    driver.close()
