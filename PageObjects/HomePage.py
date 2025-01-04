from selenium.webdriver.common.by import By


class HomePage:

    #create constructor to call driver
    def __init__(self, driver):
        self.driver = driver

    #locators
    shop = (By.LINK_TEXT, "Shop")
    name_textbox = (By.NAME, "name")
    email_textbox = (By.NAME, "email")
    password_textbox = (By.ID, "exampleInputPassword1")
    icecream_checkbox = (By.ID, "exampleCheck1")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    employment_status_employed = (By.XPATH, "//input[@value='option2']")
    dob = (By.NAME, "bday")
    submit = (By.XPATH, "//input[@value='Submit']")
    message = (By.XPATH, "//div[@class ='alert alert-success alert-dismissible']//strong")

    #method calls
    def shopField(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name_textbox)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email_textbox)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password_textbox)

    def checkboxIcecream(self):
        return self.driver.find_element(*HomePage.icecream_checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender_dropdown)

    def getWorkStatus(self):
        return self.driver.find_element(*HomePage.employment_status_employed)

    def getDOB(self):
        return self.driver.find_element(*HomePage.dob)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        message_displayed = self.driver.find_element(*HomePage.message).text
        assert message_displayed == "Success!"
        return print("Message displayed at the final confirmation page is- ", message_displayed)
