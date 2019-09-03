import unittest

from pages.apidemos_page import ApiDemosPage
from pages.base_page import BasePage
from settings.session_settings import start_session, end_session


class BaseTestCaseSet(unittest.TestCase):

    bp = None
    driver = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        """Here are functions that are run before all tests (ex. initialization of driver and BasePage """

        cls.driver = start_session()
        cls.bp = BasePage(driver=cls.driver)
        cls.bp.print_screen_size()
        cls.bp.print_screen_orientation()

        """Put here initialization of other classes/pages """

        cls.adp = ApiDemosPage(driver=cls.driver)

    def setUp(self):
        super().setUp()
        print('\nStarting new test case\n')

        """Put here functions that you want to run before every test case"""

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

    def tearDown(self):
        super().tearDown()
        self.bp.reset_app()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.bp.close_app()
        end_session(cls.driver)

