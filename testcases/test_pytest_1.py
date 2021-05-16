import inspect
import logging
import allure
from allure_commons.types import AttachmentType
import pytest
import unittest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys

from conftest import _capture_screenshot
from restapi.BaseAPI import getUsersapi


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
class Test_URL_Chrome(BasicTest):

    def test_lambdatest_todo_app(self):
        log = self.getLogger()
        log.info("Laubching URL")
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()
        titleOfWebPage = self.driver.title
        res="Google" == titleOfWebPage
        if res==True:
            log.info("Expected == Actual  Title")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="lamdatest", attachment_type=AttachmentType.PNG)
            # assert False
        # pytest.xfail("Expected Not Eqls Actual")
        log.info("Maximized window")
        time.sleep(2)
    @allure.step("launching Goggle in chrome")
    def test_lambdatest_load(self):
        log = self.getLogger()
        log.info("Laubching URL")
        self.driver.get('https://www.google.com/')
        self.driver.maximize_window()
        titleOfWebPage = self.driver.title
        res = "Googl" == titleOfWebPage
        if res == True:
            log.info("Expected == Actual  Title")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="lamdatest", attachment_type=AttachmentType.PNG)
            # assert False
        # pytest.xfail("Expected Not Eqls Actual")
        log.info("Maximized window")
        time.sleep(2)

    @allure.step("REST API Testing")
    def test_API(self):
        log = self.getLogger()
        allure.description("Executing getUsersapi")
        log.info("Executing getUsersapi")
        getUsersapi()


