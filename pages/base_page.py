import os
import random
import time

from appium.webdriver import WebElement
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from settings.main_settings import ROOT_DIR_FORWARD_SLASH_SEPARATOR


class BasePage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.orientation = self.get_screen_orientation()
        self.size = self.get_screen_size()
        self.width, self.height = self.size
        self.right_border = self.width
        self.left_border = 0
        self.upper_border = 0
        self.bottom_border = self.height

    """App navigation"""

    def go_back(self):
        self.driver.back()
        print('\nWent to previous screen')

    @staticmethod
    def wait(timer: int = 0):
        print('\nWaiting...')
        time.sleep(timer)
        print('\nWaiting end')

    def close_app(self):
        self.driver.close_app()
        print('\nApp closed')

    def reset_app(self):
        self.driver.reset()

    """Screen options"""

    def get_screen_orientation(self):
        orientation = self.driver.orientation
        return orientation

    def print_screen_orientation(self):
        statement = f'\nScreen orientation is: \n {self.orientation}'
        print(statement)
        return self.orientation

    def set_screen_orientation(self, desired_orientation: str = 'LANDSCAPE' or 'PORTRAIT'):
        current_orientation = self.orientation
        if desired_orientation == current_orientation:
            print(f'\nThere is no need to set same orientation')
        else:
            self.driver.orientation = desired_orientation
            print(f'\nScreen orientation changed to {desired_orientation}')

    def get_screen_size(self):
        width = 0
        height = 0
        counter = 1
        while width == 0 and height == 0 and counter < 15:
            size = self.driver.get_window_size()
            width = size.get('width')
            height = size.get('height')
            counter += 1
        assert width > 0 and height > 0, "\nDriver can't get screen size, framework can't work properly. Please rerun."
        return width, height

    def print_screen_size(self):
        statement = f'\nScreen size is: \n' \
            f'width: {self.width}\n' \
            f'height: {self.height}\n'
        print(statement)
        return self.width, self.height

    def get_screenshot(self, test_name: str):
        number = 0
        filename = f'{test_name.lower() + str(number)}.png'
        file_path = f'{ROOT_DIR_FORWARD_SLASH_SEPARATOR}/screenshots/{filename}'
        while os.path.exists(file_path) is True:
            number = number + 1
            filename = f'{test_name.lower() + str(number)}.png'
            file_path = f'{ROOT_DIR_FORWARD_SLASH_SEPARATOR}/screenshots/{filename}'
        return self.driver.get_screenshot_as_file(file_path)

    """Find Element"""

    def find_element_by_access_id(self, access_id):
        return self.driver.find_element_by_accessibility_id(access_id)

    def find_element_by_xpath(self, selector, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located((By.XPATH, selector)))
        return self.driver.find_element_by_xpath(selector)

    """Tapping elements functions"""

    @staticmethod
    def get_random_position_within_element(element, offset: int = 0):
        element_size = element.size
        width = element_size.get('width', 0)
        height = element_size.get('height', 0)
        assert width > 0, 'Width can not be 0'
        assert height > 0, 'Height can not be 0'
        x_random = random.randint(1 + offset, int(width) - offset)
        y_random = random.randint(1 + offset, int(height) - offset)

        return x_random, y_random

    """Tapping elements - XCUIT driver"""

    def tap_on_element_xcuit(self, element: WebElement, x: int = None, y: int = None, offset: int = 15):

        """
        If x and y are not typed, then function gets size of an element and taps randomly within the element
        if x and y are typed, then function taps at x and y screen position relative to element position
        XCUITest core method - use when developing iOS app
        """

        if x is None and y is None:
            x, y = self.get_random_position_within_element(element, offset)
            statement = f'\nTapped at: \n width: {x} \n height: {y} \n within the element'

        else:
            assert x and y, 'You should set x and y'
            statement = f'\nTapped at: \n width: {x} \n height: {y} \n relative to element position'

        params = {'element': element.id,
                  'x': x,
                  'y': y}
        self.driver.execute_script('mobile: tap', params)
        print(statement)
        return element

    def tap_on_xy_xcuit(self, x: int, y: int):

        """
        Taps at x and y position relative to screen borders
        XCUITest core method - use when developing iOS app
        """

        params = {'x': x,
                  'y': y}
        statement = f'\nTapped at: \n width: {x} \n height: {y} \n relative to screen borders'
        self.driver.execute_script('mobile: tap', params)
        return print(statement)

    """Tapping elements - UIAutomator 2 driver"""

    def tap_on_element_wda(self, element: WebElement, x: int = None, y: int = None):

        """
        Taps element without random position within this element.
        WebDriver method, could be used in iOS and Android app
        """

        tc = TouchAction(self.driver)
        if x is None and y is None:
            tc.tap(element)
            statement = f'\nTapped at element'
        else:
            assert x and y, 'You should set x and y'
            tc.tap(x=x, y=y)
            statement = f'\nTapped at: \n width: {x} \n height: {y} \n relative to screen borders'
        tc.perform()
        print(statement)
        return tc

    def press_wda(self, element: WebElement, x: int, y: int):

        """WebDriver method, could be used in iOS and Android app"""

        tc = TouchAction(self.driver)
        if x is None and y is None:
            tc.press(element)
            statement = f'\nPressed an element'
        else:
            assert x and y, 'You should set x and y'
            tc.press(x=x, y=y)
            statement = f'\nPressed at: \n width: {x} \n height: {y} \n relative to screen borders'
        tc.perform()
        print(statement)
        return tc

    """Swipes - XCUIT driver"""

    def flick_xcuit(self, direction: str):

        """
        This method simulates short movement of finger (flick)
        XCUITest core method - use when developing iOS app
        """

        self.driver.execute_script('mobile: swipe', {'direction': direction})
        statement = f'\nSwiped {direction} shortly'
        return print(statement)

    def flick_right_xcuit(self):
        return self.flick_xcuit('right')

    def flick_left_xcuit(self):
        return self.flick_xcuit('left')

    def flick_up_xcuit(self):
        return self.flick_xcuit('up')

    def flick_down_xcuit(self):
        return self.flick_xcuit('down')

    def swipe_xcuit(self, duration: float or int, from_x: float or int,
                    from_y: float or int, to_x: float or int, to_y: float or int):

        """
        This method simulates long move (drag) of the finger
        XCUITest core method - use when developing iOS app
        """

        params = {'duration': duration,
                  'fromX': from_x,
                  'fromY': from_y,
                  'toX': to_x,
                  'toY': to_y}
        statement = f'\nSwiping from {from_x}, {from_y} to {to_x}, {to_y}.'
        print(statement)
        return self.driver.execute_script('mobile: dragFromToForDuration', params), print('Swiped\n')

    def swipe_right_xcuit(self):
        swipe_start = self.left_border + 1
        swipe_stop = self.right_border
        swipe_height = self.height * 0.5
        return self.swipe_xcuit(duration=1.0,
                                from_x=swipe_start,
                                from_y=swipe_height,
                                to_x=swipe_stop,
                                to_y=swipe_height)

    def long_swipe_left_xcuit(self):
        swipe_start = self.right_border - 1
        swipe_stop = self.left_border
        swipe_height = self.height * 0.5
        return self.swipe_xcuit(duration=1.0,
                                from_x=swipe_start,
                                from_y=swipe_height,
                                to_x=swipe_stop,
                                to_y=swipe_height)

    def long_swipe_up_xcuit(self):
        swipe_start = self.bottom_border * 0.98
        swipe_stop = self.upper_border
        swipe_width = self.width * 0.5
        return self.swipe_xcuit(duration=1.0,
                                from_x=swipe_width,
                                from_y=swipe_start,
                                to_x=swipe_width,
                                to_y=swipe_stop)

    def long_swipe_up_with_control_center_xcuit(self):

        """Doesn't work yet"""

        return self.swipe_xcuit(duration=1.0,
                                from_x=180.0,
                                from_y=667.0,
                                to_x=180.0,
                                to_y=1.0)

    def long_swipe_down_xcuit(self):
        swipe_start = self.upper_border * 0.37
        swipe_stop = self.bottom_border
        swipe_width = self.width * 0.5
        return self.swipe_xcuit(duration=1.0,
                                from_x=swipe_width,
                                from_y=swipe_start,
                                to_x=swipe_width,
                                to_y=swipe_stop)

    def long_swipe_down_with_menu_bar_xcuit(self):
        swipe_start = self.upper_border
        swipe_stop = self.bottom_border
        swipe_width = self.width * 0.5
        return self.swipe_xcuit(duration=1.0,
                                from_x=swipe_width,
                                from_y=swipe_start,
                                to_x=swipe_width,
                                to_y=swipe_stop)

    """Swipes - UIAutomator 2 driver"""

    def swipe_wda(self, from_x: float or int, from_y: float or int, duration_of_press: float or int,
                  to_x: float or int, to_y: float or int):

        """
        This method should be used if methods above don't work. Contains waits after
        every action, because sometimes Appium read chain of actions separately instead as a action chain.
        WebDriver method, could be used in iOS and Android app
        """

        swipe = TouchAction(driver=self.driver).long_press(el=None, x=from_x, y=from_y, duration=duration_of_press) \
            .wait(500) \
            .move_to(el=None, x=to_x, y=to_y) \
            .wait(500) \
            .release()
        statement = f'\nSwiping from {from_x}, {from_y} to {to_x}, {to_y}.'
        print(statement)
        return swipe.perform()

    def swipe_right_wda(self):
        swipe_start = self.left_border + 1
        swipe_stop = self.right_border
        swipe_height = self.height * 0.5
        return self.swipe_wda(duration_of_press=1000,
                              from_x=swipe_start,
                              from_y=swipe_height,
                              to_x=swipe_stop,
                              to_y=swipe_height)

    def swipe_left_wda(self):
        swipe_start = self.right_border - 1
        swipe_stop = self.left_border
        swipe_height = self.height * 0.5
        return self.swipe_wda(duration_of_press=1000,
                              from_x=swipe_start,
                              from_y=swipe_height,
                              to_x=swipe_stop,
                              to_y=swipe_height)

    def swipe_up_wda(self):
        swipe_start = self.bottom_border * 0.98
        swipe_stop = self.upper_border
        swipe_width = self.width * 0.5
        return self.swipe_wda(duration_of_press=1000,
                              from_x=swipe_width,
                              from_y=swipe_start,
                              to_x=swipe_width,
                              to_y=swipe_stop)

    def swipe_down_wda(self):
        swipe_start = self.upper_border * 0.37
        swipe_stop = self.bottom_border
        swipe_width = self.width * 0.5
        return self.swipe_wda(duration_of_press=1000,
                              from_x=swipe_width,
                              from_y=swipe_start,
                              to_x=swipe_width,
                              to_y=swipe_stop)

    def swipe_down_with_with_menu_bar_wda(self):
        swipe_start = self.upper_border
        swipe_stop = self.bottom_border
        swipe_width = self.width * 0.5
        return self.swipe_wda(duration_of_press=1000,
                              from_x=swipe_width,
                              from_y=swipe_start,
                              to_x=swipe_width,
                              to_y=swipe_stop)

    """Fields functions"""

    @staticmethod
    def send_keys_wda(keys: str, element: WebElement):
        element.send_keys(keys)
        print(f'\nSent: \n{keys} \nto the element')
        return element

    @staticmethod
    def clear_field_wda(element: WebElement):
        element.clear()
        print('\nElement cleared')
        return element
