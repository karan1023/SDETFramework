from pageObject.AddLead import AddLead
from pageObject.LoginObject import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import Xlutils
import time

class Test_AddLeads:

    baseUrl = ReadConfig.getBaseUrl()
    path = './/testData/TestData.xlsx'
    logger = LogGen.loggen()

    def test_addlead(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.logger.info('Browser launched and URL opened')
        self.lp = Login(self.driver)
        self.lp.setUserName('admin')
        self.lp.setPassword('admin@123')
        self.lp.setCaptcha()
        # time.sleep(8)
        self.lp.clickLogin()
        self.logger.info('Admin Login Successful')
        self.al = AddLead(self.driver)
        time.sleep(8)
        self.al.clickAddLeads()
        self.al.setName('SecondDec LeadOne')
        self.al.setEmail('2janlead1@yopmail.com')
        self.al.setMobile('9999020101')
        self.al.setCity()
        self.al.setSource()
        self.al.setSubsource()
        self.al.clickSave()
        self.driver.close()