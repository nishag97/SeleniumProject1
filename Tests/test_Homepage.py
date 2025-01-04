import time
import pytest

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()

        log.info("Form submission POM")
        print("Form submission POM")
        windowTitle = self.driver.title
        print("Url Title is-> ", windowTitle)

        homepage = HomePage(self.driver)

        #hard code
        #homepage.getName().send_keys("NISHI")
        # datadriven
        homepage.getName().send_keys(getData["firstname"])

        homepage.getEmail().send_keys("nishi@est.com")
        homepage.getPassword().send_keys("test000")
        homepage.checkboxIcecream().click()

        self.selectOptionsByText(homepage.getGender(), getData["gender"])

        time.sleep(1)
        homepage.getWorkStatus().click()
        time.sleep(2)
        homepage.getDOB().send_keys("05/08/1997")
        time.sleep(4)
        homepage.submitForm().click()

        time.sleep(1)
        homepage.getSuccessMessage()
        log.info("SUCCESSS PAASS TEST HOMEPAGE")
        self.driver.refresh()

    #Instead of giving hard code values, use data driver parameterization method to give data set directly using fixtures with params
    #here I have given 2 data sets using tuples, but you may give one set as well.
    # EXAMPLE- (params=[("Dhruv", "nishi@test.k", "Male")])
    # [] LIST, () TUPLE
    # {} DICTIONARY Use Key value pair to give key names to each value
    # EXAMPLE of 2 dictionaries- (params=[{"firstname":"Dhruv", "emailId":"nishi@test.k", "gender":"Male"}, {"firstname":"ANJANA", "emailId":"test2e@", "gender":"Female"}])
    # removing these big param data sets from here to separate data class to make data more optimise at one place(class)
    @pytest.fixture(params=HomePageData.getTestData("T4"))
    def getData(self, request):
        return request.param
