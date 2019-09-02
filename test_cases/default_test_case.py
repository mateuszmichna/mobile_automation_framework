import unittest

from pages.apidemos_page import ApiDemosPage
from pages.base_page import BasePage
from settings.session_settings import start_session, end_session


class BaseTestCaseSet(unittest.TestCase):

    """Put here functions that should be run before full set of test cases and initialization of classes """

    driver = start_session()
    bp = BasePage(driver=driver)
    adp = ApiDemosPage(driver=driver)

    def setUp(self):
        super().setUp()

        """Put here functions that you want to run before every test case"""

        self.bp.print_screen_size()
        self.bp.print_screen_orientation()
        self.bp.reset_app()

    def test_first(self):
        self.adp.tap_views()
        self.bp.go_back()
        self.adp.tap_views()
        self.bp.swipe_up_wda()
        self.bp.swipe_up_wda()
        self.bp.swipe_up_wda()
        self.adp.tap_Text_Fields()
        self.adp.tap_txt_field()
        self.adp.send_keys_to_txt_field('test test test')
        self.bp.wait(3)
        self.adp.clear_txt_field()
        self.bp.wait(3)

    def test_second(self):
        self.adp.set_screen_orientation('PORTRAIT')
        self.adp.set_screen_orientation('LANDSCAPE')
        self.bp.wait(3)
        self.bp.print_screen_orientation()
        self.bp.wait(3)

    def test_this_is_always_last_test_case_in_set(self):
        self.bp.close_app()
        end_session(self.driver)

    def tearDown(self):
        super().tearDown()

