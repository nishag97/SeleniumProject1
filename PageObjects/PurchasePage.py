from selenium.webdriver.common.by import By


class PurchasePage:
    productListed = (By.XPATH, "//tr//h4[@class='media-heading']//a")
    finalCheckout = (By.XPATH, "//button[@class= 'btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getProductsSelected(self):
        return self.driver.find_elements(*PurchasePage.productListed)

    def getCheckout(self):
        return self.driver.find_element(*PurchasePage.finalCheckout)
