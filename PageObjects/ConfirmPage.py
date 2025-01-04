from selenium.webdriver.common.by import By

class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryField = (By.ID,"country")
    countrySuggestions = (By.XPATH, "//div[@class ='suggestions']//ul//li/a")
    purchaseButton = (By.XPATH, "//input[@value='Purchase']")
    message = (By.XPATH, "//div[@class ='alert alert-success alert-dismissible']//strong")

    def addCountryName(self, desiredCountry):
        print("Given country name is- ", desiredCountry)
        return self.driver.find_element(*ConfirmPage.countryField).send_keys(desiredCountry)

    def getCountrySuggestions(self):
        #use select options here instead of hard code sleep pattern
        return self.driver.find_element(*ConfirmPage.countrySuggestions).click()

    def getPurchaseItems(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton).click()

    def getSuccessMessage(self):
        message_displayed = self.driver.find_element(*ConfirmPage.message).text
        assert message_displayed == "Success!"
        return print("Message displayed at the final confirmation page is- ", message_displayed)
