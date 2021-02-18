from selenium.webdriver import ActionChains
import time
import re


class AddLead:

    # Elements XPath
    leads_menu_xpath = '//*[@id="root"]/div/header/nav/ul/li[1]/a'
    addlead_submenu_xpath = '//a[@href="/add-leads"]'
    name_txtbox_xpath = '//*[@id="user_name"]'
    email_txtbox_xpath = '//*[@id="userEmail"]'
    mobile_txtbox_xpath = '//*[@id="user_mobile"]'
    city_drpdwn_xpath = '//*[@id="city"]/div/div[1]'
    source_drpdwn_xpath = '//*[@id="source"]'
    subsource_drpdwn_xpath = '//*[@id="subSource"]'
    premium_checkbox_xpath = '//*[@id="isPremium"]'
    save_btn_xpath = '//button[contains(text(),Save)]'

    # Action Methods
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def clickAddLeads(self):
        leads = self.driver.find_element_by_xpath(self.leads_menu_xpath)
        addleads = self.driver.find_element_by_xpath(self.addlead_submenu_xpath)
        self.actions.move_to_element(leads).move_to_element(addleads).click().perform()

    def setName(self, name):
        self.driver.find_element_by_xpath(self.name_txtbox_xpath).clear()
        self.driver.find_element_by_xpath(self.name_txtbox_xpath).send_keys(name)

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.email_txtbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_txtbox_xpath).send_keys(email)

    def setMobile(self, mobile):
        self.driver.find_element_by_xpath(self.mobile_txtbox_xpath).clear()
        self.driver.find_element_by_xpath(self.mobile_txtbox_xpath).send_keys(mobile)

    def setCity(self):
        self.driver.find_element_by_xpath(self.city_drpdwn_xpath).click()
        self.driver.find_element_by_id("react-select-10-option-3").click()

    def setSource(self):
        self.driver.find_element_by_xpath(self.source_drpdwn_xpath).click()
        self.driver.find_element_by_id("react-select-11-option-1").click()

    def setSubsource(self):
        self.driver.find_element_by_xpath(self.subsource_drpdwn_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_id("react-select-12-option-0").click()

    def clickSave(self):
        self.driver.find_element_by_xpath(self.save_btn_xpath).click()
        time.sleep(2)
        toast_text = self.driver.find_element_by_xpath("//div[@class='Toastify__toast-body']").text
        pattern = '\ALead'
        if re.match(pattern, toast_text):
            assert True
        else:
            assert False
