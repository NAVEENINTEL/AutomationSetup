import allure
from allure_commons.types import AttachmentType
import pytest
from selenium.webdriver.common.by import By
import time
from utilities.BasicTest import BasicTest

@pytest.mark.usefixtures("setup1")
class Test_URL_Chrome(BasicTest):
    @allure.description("Launching Amazon website and search for Iphone")
    def test_amazon2(self):
        allure.attach('Tester', 'Naveen')
        with allure.step('Launching amazon website'):
            log = self.getLogger()
            log.info("Launching amazon website")
            self.driver.get('https://www.amazon.in')
            self.driver.maximize_window()
        with allure.step('Searching for Iphone'):
            self.driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Iphone")
            self.driver.find_element(By.XPATH, "//*[@id='nav-search-bar-form']/div[3]/div").click()
            time.sleep(1)
    def test_lambdatest_todo_app(self):
        allure.attach("Tester","Naveen")
        log = self.getLogger()
        log.info("Launching URL")
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



