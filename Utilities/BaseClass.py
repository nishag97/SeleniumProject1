import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    # def __init__(self, *args, **kwargs):
    #     self.log = logging.getLogger(self.__class__.__name__)
    #add re-usable methods here to reuse among all classes since baseclass will be inherited by all child classes
    def selectOptionsByText(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def getLogger(self):

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        filehandler = logging.FileHandler('logFile.log')
        #log file will be auto created at run time.
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        # connection made between logging and logger
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        return logger

