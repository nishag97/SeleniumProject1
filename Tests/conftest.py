import pytest
from selenium import webdriver
driver = None
#Add only common fixtures here

# Making browser selections done from here
# https://docs.pytest.org/en/stable/example/simple.html#how-to-change-command-line-options-defaults
# cmd to give required browser name for automation: py.test --browser_name firefox --html=report.html -s
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
#use this request which is an instance of a fixture method
def setup(request):
    global driver
    requiredBrowser = request.config.getoption("browser_name")

    if requiredBrowser == "chrome":
        driver = webdriver.Chrome()

    elif requiredBrowser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Ie()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    #we can't use return statement with yield keyword so here is the alternative
    #we use request here to pass this method's driver into instance class driver,
    #so wherever this fixture method use they can add their local driver into this main setup driver.
    request.cls.driver = driver
    yield
    driver.close()

    #to create html report, IN terminal- open folder/package where your all pytest present.
    #Then generate html report by using this command py.test --html=report.html -s
