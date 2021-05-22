import pytest
from selenium import webdriver

def setup():
    browser=""
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome(executable_path=r'D:\python practice\Automation\chromedriver.exe')
        print("Launching chrome browser.........")
        # driver.maximize_window()
    return driver
