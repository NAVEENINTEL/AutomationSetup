import pytest
import time

from utilities.BasicTest import BasicTest


@pytest.mark.usefixtures("setup1")
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


