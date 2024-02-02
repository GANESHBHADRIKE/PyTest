import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
'''
test case are indicate using                 def test_anyname():
you have to pass the module name to the testcase 

'''

@pytest.fixture(scope="module")
def setup_module():

    global driver
    print("----------------------setup-----------------------")
    service_obj = Service("C:\\Users\\Ganesh Bhadrike\\eclipse-workspace\\selenium\\driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    yield
    print("----------------------tear down-----------------------")
    driver.quit()


def test_google_tittle(setup_module):
    assert driver.title == "Google"


def test_google_url(setup_module ):
    assert driver.current_url == "https://www.google.com/"