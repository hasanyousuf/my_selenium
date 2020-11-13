# Requirements
##	Sumit checkout request
## Valid for each field
## All combinations must function
## Hearing any other requirement

#####
# Looking in HTML of code, it is using HTML5 required feature
# As this does not change in DOM, it should be handled in custom 
# error handling class 
# How to Solve (Approach)
###### Open browser
###### Without filling any field press submit button, it should not display confirmation page 
###### Check field is displayed
###### Check field is enabled
###### Check if there is "required" attribute for the field
###### Fill the field
###### Repeat these step until the last field where required attribute is present
#####  Finally submit the page and verify from the confiramtion message 


######### Improvements #########
# Page Object Model should be used
# More classes can be added to extend the tests to make it more towards Framework
# Adding nice reporting tools can provide clear visitibilty


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import os
import time


# Class to handle Test
class TestMust:

    @pytest.fixture()
    def setup(self):
        #Installing Chrome driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #maximizing browser window
        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)
        value = os.getenv("web_home")
        # Print the value of 'web_home'
        # environment variable
        print("Value of 'web_home' environment variable :", value)
        self.driver.get(value)
        yield "resource"
        self.driver.quit()

    ## Test data
    testdata2 =[(("id_company_name","id","Hero company"), ("id_admin_email","id","company email"),
                 ("id_admin_first_name","id","first name"),("id_admin_last_name","id","Last name"),
                 ("id_product_0","id","aa"),(".fluid > input","css",""))]

    @pytest.mark.parametrize("company, email, firstname,lastname,product,submit", testdata2)
    def test_page(self, setup, company, email, firstname,lastname,product,submit ):
        variables = [company, email, firstname,lastname,product,submit]
        ##To findout how many fields are available in the form
        data = self.driver.find_elements(By.XPATH, "//input")
        print(len(variables))
        for i in variables:
            submit_page=self.driver.find_element(By.CSS_SELECTOR, ".fluid > input").click()
            time.sleep(1)
            try:
                if(i[1]=="id"):
                    handle=self.driver.find_element(By.ID, i[0])
                    field_type=handle.get_attribute("type")
                    #field_requirgited=
                    if field_type == "text" and handle.is_displayed() and handle.is_enabled() and \
                            handle.get_attribute("required"):
                        self.driver.find_element(By.ID, i[0]).send_keys(i[2])
                    else:
                        self.driver.find_element(By.ID, i[0]).click()
                else:
                    self.driver.find_element(By.CSS_SELECTOR, i[0]).click()

            except Exception :
                print("Form field exception")
        try:
            #id_company_name
            #confirmation=self.driver.find_element(By.ID, "confirmation_id")
            confirmation = self.driver.find_element(By.ID, "id_company_name").get_attribute("value")
            print(confirmation)

        except NoSuchElementException:

            assert confirmation.text !="confirmation"