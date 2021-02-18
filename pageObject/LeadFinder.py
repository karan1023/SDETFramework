class Filter:

    # Dashboard Filters Xpath
    searchBy_drpdwn_xpath = '//*[@id="root"]/div/div[2]/div/div[2]/div/ul/li[1]'
    searchBy_name_xpath = '//*[@id="react-select-2-option-1"]'
    searchBy_leadid_xpath = '//*[@id="react-select-2-option-0"]'
    search_txtbox_xpath = '//*[@id="search_input"]'
    cluster_txtbox_xpath = '//input[@id="cluster"]'
    search_btn_xpath = '//*[@type="submit"]'

    #Action Method
    def __init__(self, driver):
        self.driver = driver

    def clickSearchBy(self):
        self.driver.find_element_by_xpath(self.searchBy_drpdwn_xpath).click()

    def selectSearchByName(self):
        self.driver.find_element_by_xpath(self.searchBy_name_xpath).click()

    def clickSearchByTextbox(self):
        self.driver.find_element_by_xpath(self.search_txtbox_xpath).click()
        self.driver.find_element_by_xpath(self.search_txtbox_xpath).send_keys("Karan")

    def clickSearchBtn(self):
        self.driver.find_element_by_xpath(self.search_btn_xpath).click()