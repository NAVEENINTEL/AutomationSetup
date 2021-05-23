from urllib import request
from webdriver_manager.chrome import ChromeDriverManager
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager, EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="firefox"
    )

@pytest.fixture(scope="class")
def setup1(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name=='chrome':
        web_driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        #web_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name=='firefox':
        web_driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name=='IE':
        web_driver=driver = webdriver.Ie(IEDriverManager().install())
    elif browser_name=='edge':
        web_driver=webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
    #     # web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")

    request.cls.driver = web_driver
    yield
    web_driver.close()

def driver_init_1(request):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('headless')
    # web_driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="chromedriver.exe")
    # web_driver = webdriver.Remote( command_executor='http://localhost:4444/wd/hub',desired_capabilities={
    #         "browserName": "firefox",
    #         "platformName": "linux",
    #     })
    # web_driver = webdriver.Chrome(executable_path="C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
    web_driver=webdriver.Chrome(ChromeDriverManager().install())
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