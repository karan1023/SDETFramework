import pytest

from pageObject.LeadFinder import Filter
from pageObject.LoginObject import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_LeadFinder:

    baseUrl = ReadConfig.getBaseUrl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_search_lead(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName('admin')
        self.lp.setPassword('admin@123')
        self.lp.setCaptcha()
        self.lp.clickLogin()
        self.lf = Filter(self.driver)
        time.sleep(10)
        self.lf.clickSearchBy()
        time.sleep(10)
        self.lf.selectSearchByName()
        self.lf.clickSearchByTextbox()
        self.lf.clickSearchBtn()
        self.driver.close()

