import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
'''
I HAd automated a flipcart website for the demo purpose
you will need the conftest.py file to run this file


'''

# @pytest.fixture(scope="class")          # we are using the class fixture 
# def setup_module(request):              #CREATE A REQUEST 

#     global driver
#     print("----------------------setup-----------------------")
#     service_obj = Service("C:\\Users\\Ganesh Bhadrike\\eclipse-workspace\\selenium\\driver\\chromedriver.exe")
#     driver = webdriver.Chrome(service=service_obj)
#     request.cls.driver = driver             # CREATING A REQUEST CLASS OF A DRIVER 
#     driver.implicitly_wait(10)
#     driver.delete_all_cookies()
#     driver.get("https://www.flipkart.com/")
#     yield
#     print("----------------------tear down-----------------------")
#     driver.quit()


@pytest.mark.usefixtures("setup_module")                    # USING THE MODULE TO MARK THE FIXTURE
class Test_Base_class:  
    pass


class Test_Google(Test_Base_class):

    def test_HomePage(self):                                # 1st testcase 

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        # launching the application 
        
        print(self.driver.title)
        print(self.driver.current_url)

        #   Search bar
        search = self.driver.find_element(By.CSS_SELECTOR, "input.Pke_EE").send_keys("mobile")

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        mobiles = self.driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
        # Fetching all the names of the mobile device and clicking on the second item present...
        for mobile in mobiles:
            print(mobile.text)
        if len(mobiles) >= 2:
            mobiles[1].click()
                
        else:
            print("not enough elements found")
            

    def test_firstpage(self):                           # 2nd testcase

        
        all_windows = self.driver.window_handles

        # Switch to the child window (assuming it's the second window in the list, adjust index if needed)
        child_window = all_windows[1]
        self.driver.switch_to.window(child_window)
        print("switch")
        cart = self.driver.find_element(By.XPATH,"//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
        actual_text = cart.text
        print(actual_text)
        expected_text = "ADD TO CART"

        if actual_text == expected_text:
            cart.click()
            print("Item Added successfully")

        self.driver.find_element(By.CSS_SELECTOR,"button[class='_2KpZ6l _2ObVJD _3AWRsL']").click()
        cont = self.driver.find_element(By.CSS_SELECTOR,"button[class='_2KpZ6l _20xBvF _3AWRsL']").text
        exp_continue = "CONTINUE"

        assert cont == exp_continue,  f"Assertion Error: Actual Title: {cont}, Expected Title: {exp_continue}"
        print("Title is as expected:", exp_continue)

        self.driver.back()
        time.sleep(2)
        self.driver.back()
        time.sleep(5)


        self.driver.find_element(By.CSS_SELECTOR,"div.YUhWwv").click()
        time.sleep(10)
        self.driver.execute_script("window.scrollBy(0,200)")
        self.driver.find_element(By.XPATH,"//div[@class='_3dsJAO'][2]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//div[@class='_3dsJAO _24d-qY FhkMJZ']").click()
        time.sleep(10)