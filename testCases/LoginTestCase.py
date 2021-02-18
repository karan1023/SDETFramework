from pageObject.LoginObject import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_title(self, setup):
        self.logger.info('******START*********')
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == 'UB :: Carmudi':
            self.driver.close()
            self.logger.info('title test case passed')
            assert True
        else:
            self.driver.save_screenshot('screenshot/'+'test_title.png')
            self.driver.close()
            self.logger.info('title test case failed')
            assert False

    def test_Login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.setCaptcha()
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'UB :: Carmudi':
            self.driver.close()
            self.logger.info('login test case passed')
            assert True
        else:
            self.driver.save_screenshot('screenshot/' + 'test_login.png')
            self.driver.close()
            self.logger.error('login test case failed')
            assert False
