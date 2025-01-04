from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getCardFooter(self):
        print("Get Card footer ", len(self.driver.find_elements(*CheckoutPage.cardFooter)))
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

