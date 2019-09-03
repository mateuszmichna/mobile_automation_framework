from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from settings.main_settings import DESIRED_CAPABILITIES, SERVER_ADDRESS, IMPLICITLY_WAIT


def start_session():
    driver = webdriver.Remote(SERVER_ADDRESS, DESIRED_CAPABILITIES)
    driver.implicitly_wait(IMPLICITLY_WAIT)
    print('\nConnected to the device\n')
    return driver


def get_session_desired_capabilites(driver: WebDriver):
    des_cap = driver.desired_capabilities
    print(f'\nDesired capabilities of this session are: \n {des_cap}')
    return des_cap


def end_session(driver: WebDriver):
    driver.quit()
