import inspect
import logging

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys

@pytest.mark.usefixtures("driver_init_1")
class BasicTest:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('../logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
class Test_URL_Firefox(BasicTest):
    def test_google_search(self):
        log = self.getLogger()
        log.info("Laubching URL3")
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        title = "Google"
        assert title == self.driver.title
        time.sleep(2)

    def test_lambdatest_blog_load(self):
        log = self.getLogger()
        log.info("Laubching URL4")
        self.driver.get('https://www.lambdatest.com/blog/')
        self.driver.maximize_window()
        time.sleep(2)


