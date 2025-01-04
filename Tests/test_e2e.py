import time
from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from PageObjects.PurchasePage import PurchasePage
from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):

    #self param is mandatory if you declare method under class.
    def test_e2e(self):
        print("FIRST TEST FROM FRAMEWORK DESIGN")
        print("Url Title is-> ", self.driver.title)
        homepage = HomePage(self.driver)
        homepage.shopField().click()
        time.sleep(1)

        print("SECOND TEST FROM FRAMEWORK DESIGN")
        checkout = CheckoutPage(self.driver)
        cards = checkout.getCardTitles()
        number = len(cards)
        print("length of items is ", number)
        i = -1
        for card in cards:
            i = i + 1
            cardName = card.text
            print("card text is ", cardName)
            if cardName == "Samsung Note 8":
                checkout.getCardFooter()[i].click()

        checkout.getCheckoutButton().click()
        time.sleep(2)

        purchasepage = PurchasePage(self.driver)
        selected_items = purchasepage.getProductsSelected()
        print("Total selected items in cart-", len(selected_items))

        for item in selected_items:
            item_name = item.text
            print("Item text is ", item_name)
            if item_name == "Samsung Note 8":
                print("nameofSelectedItem in cart is ", item_name)
                break

        time.sleep(1)
        purchasepage.getCheckout().click()
        time.sleep(1)

        confirmpage = ConfirmPage(self.driver)
        country = "India"
        confirmpage.addCountryName(country)
        time.sleep(10)
        confirmpage.getCountrySuggestions()
        time.sleep(2)
        confirmpage.getPurchaseItems()
        time.sleep(1)
        confirmpage.getSuccessMessage()
        time.sleep(2)

