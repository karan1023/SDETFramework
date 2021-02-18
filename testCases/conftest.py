from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path='/home/karanthakur/PycharmProjects/SDETFramework/Driver/chromedriver')
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='/home/karanthakur/PycharmProjects/SDETFramework/Driver/geckodriver')
        return driver
    else:
        driver = webdriver.Ie(executable_path='/home/karanthakur/PycharmProjects/SDETFramework/Driver/geckodriver')
        return driver


def pytest_addoption(parser):  #This will get the browser value from command line
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  #This will return the browser value to setup method
    return request.config.getoption('--browser')

########## Pytest HTML Report ##########

#It is a hook for Adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'UB Ph'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Karan Thakur'


#It is a hook for Deleting/modifying environment info from HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
