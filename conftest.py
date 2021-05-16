from urllib import request

import allure
import pytest
from allure_commons.types import AttachmentType

from selenium import webdriver

# from hello import driver


@pytest.fixture(scope="class")
def driver_init_1(request):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    # web_driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="chromedriver.exe")
    web_driver = webdriver.Remote( command_executor='http://localhost:4444/wd/hub',desired_capabilities={
            "browserName": "firefox",
            "platformName": "linux",
        })
    # web_driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()
@pytest.fixture(scope="class")
def driver_init_2(request):
    # firefox_options=webdriver.FirefoxOptions()
    # firefox_options.set_headless()
    # web_driver = webdriver.Firefox(firefox_options=firefox_options,executable_path="geckodriver.exe")
    # web_driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4444/wd/hub')
    web_driver = webdriver.Firefox(executable_path="geckodriver.exe")
    request.cls.driver = web_driver
    yield
    web_driver.close()

def _capture_screenshot(name):
        allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)