import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Here we had use the fixture scope as module
@pytest.fixture(scope="module")
def setup_module():                    # so setup_module is the module of the fixture

    global driver
    print("----------------------setup-----------------------")
    service_obj = Service("C:\\Users\\Ganesh Bhadrike\\eclipse-workspace\\selenium\\driver\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.flipkart.com/")
    yield
    print("----------------------tear down-----------------------")
    driver.quit()


def test_HomePage(setup_module):                    # and here we are using the module in the testcase parameter 

    driver.implicitly_wait(10)
    driver.maximize_window()
    # launching the application 
    
    print(driver.title)
    print(driver.current_url)

    #   Search bar
    search = driver.find_element(By.CSS_SELECTOR, "input.Pke_EE").send_keys("mobile")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    mobiles = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
    # Fetching all the names of the mobile device and clicking on the second item present...
    for mobile in mobiles:
        print(mobile.text)
    if len(mobiles) >= 2:
        mobiles[1].click()
            
    else:
        print("not enough elements found")
            

def test_firstpage(setup_module):                   # and here we are using the module in the testcase parameter 

    
    all_windows = driver.window_handles

    # Switch to the child window (assuming it's the second window in the list, adjust index if needed)
    child_window = all_windows[1]
    driver.switch_to.window(child_window)
    print("switch")
    cart = driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
    actual_text = cart.text
    print(actual_text)
    expected_text = "ADD TO CART"

    if actual_text == expected_text:
        cart.click()
        print("Item Added successfully")

    driver.find_element(By.CSS_SELECTOR,"button[class='_2KpZ6l _2ObVJD _3AWRsL']").click()
    cont = driver.find_element(By.CSS_SELECTOR,"button[class='_2KpZ6l _20xBvF _3AWRsL']").text
    exp_continue = "CONTINUE"

    assert cont == exp_continue,  f"Assertion Error: Actual Title: {cont}, Expected Title: {exp_continue}"
    print("Title is as expected:", exp_continue)

    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(5)


    driver.find_element(By.CSS_SELECTOR,"div.YUhWwv").click()
    time.sleep(10)
    driver.execute_script("window.scrollBy(0,200)")
    driver.find_element(By.XPATH,"//div[@class='_3dsJAO'][2]").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//div[@class='_3dsJAO _24d-qY FhkMJZ']").click()
    time.sleep(10)