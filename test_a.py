from datetime import datetime
import pdb

def test_Openurl(setup):
    pdb.set_trace()
    driver = setup["driver"]
    url = setup["url"]
    
    try:
        before_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
        driver.get(url)
        now_time = datetime.now().strftime('%H%M%S%f')  #  Timestamp
    except Exception as e:
        print(e.message)
    
    assert driver.current_url == url
    driver.save_screenshot("ss.png")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.save_screenshot("ss1.png")
    driver.close()
