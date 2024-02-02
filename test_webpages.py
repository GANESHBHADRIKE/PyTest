import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service




def test_google():
    service_obj = Service("C:\\Users\\Ganesh Bhadrike\\eclipse-workspace\\selenium\\driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.google.com/")
    assert driver.title == "Google"
    driver.quit()


def test_facebook():
    service_obj = Service("C:\\Users\\Ganesh Bhadrike\\eclipse-workspace\\selenium\\driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.facebook.com/")
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()


def test_instagram():
    service_obj = Service("C:\\Users\\Ganesh Bhadrike\\eclipse-workspace\\selenium\\driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.instagram.com/")
    assert driver.title == "Instagram"
    driver.quit()