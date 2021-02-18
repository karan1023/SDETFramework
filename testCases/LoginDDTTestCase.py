from pageObject.LoginObject import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import Xlutils
import time


class Test_001_Login:

    baseUrl = ReadConfig.getBaseUrl()
    path = './/testData/TestData.xlsx'
    logger = LogGen.loggen()

    def test_Login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.logger.info('Browser launched and URL is passed')
        self.lp = Login(self.driver)
        row_count = Xlutils.getRow(self.path, 'Sheet1')
        print('Number of rows is', row_count)
        self.outcome = []
        for r in range(2, row_count+1):
            self.username = Xlutils.readData(self.path, 'Sheet1', r, 1)
            self.password = Xlutils.readData(self.path, 'Sheet1', r, 2)
            self.result = Xlutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.setCaptcha()
            self.lp.clickLogin()
            time.sleep(10)
            cur_url = self.driver.current_url
            if cur_url == 'http://ub-phbeta.gaadi.com/':
                if self.result == 'Pass':
                    self.outcome.append('Pass')
                    self.logger.info('login test case passed')
                    self.lp.logout()
                else:
                    self.outcome.append('Fail')
                    self.logger.info('login test case failed')
                    self.lp.logout()
            else:
                if self.result == 'Fail':
                    self.outcome.append('Pass')
                    self.logger.info('login test case passed')
                else:
                    self.outcome.append('Fail')
                    self.logger.error('login test case failed')
            if 'Fail' not in self.outcome:
                assert True
        self.driver.close()
