import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")          # we are using the class fixture 
def setup_module(request):              #CREATE A REQUEST 

    global driver
    print("----------------------setup-----------------------")
    service_obj = Service("C:\\Users\\Ganesh Bhadrike\\eclipse-workspace\\selenium\\driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    request.cls.driver = driver             # CREATING A REQUEST CLASS OF A DRIVER 
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.flipkart.com/")
    yield
    print("----------------------tear down-----------------------")
    driver.quit()