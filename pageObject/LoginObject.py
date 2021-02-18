import time
from selenium.webdriver import ActionChains


class Login:
    username_textbox_xpath = '//*[@id="user_name"]'
    password_textbox_xpath = '//*[@id="password"]'
    captcha_textbox_xpath = '//*[@id="captcha"]'
    login_btn_xpath = '//*[@id="homePage"]/div/div/div/div[2]/div/div/form/div/div[5]/button'
    admin_menu_xpath = '//*[@id="root"]/div/header/nav/ul/li[5]/a'
    logout_link_xpath = '//*[@id="root"]/div/header/nav/ul/li[5]/ul/li[2]/a'


    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def setCaptcha(self):
        self.driver.find_element_by_xpath(self.captcha_textbox_xpath).click()
        time.sleep(6)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()

    def logout(self):
        admin = self.driver.find_element_by_xpath(self.admin_menu_xpath)
        logout = self.driver.find_element_by_xpath(self.logout_link_xpath)
        self.actions.move_to_element(admin).move_to_element(logout).click().perform()

