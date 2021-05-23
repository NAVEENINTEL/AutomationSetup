import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.BasicTest import BasicTest


@pytest.mark.usefixtures("setup1")
class Test_Search(BasicTest):
    def test_iphone_search(self):
        log = self.getLogger()
        log.info("Launching amazon website")
        self.driver.get('https://www.amazon.in')
        self.driver.maximize_window()
        self.driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Iphone")
        self.driver.find_element(By.XPATH,"//*[@id='nav-search-bar-form']/div[3]/div").click()
        time.sleep(1)


