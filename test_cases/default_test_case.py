import unittest

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

    def setUp(self):
        super().setUp()
        print('\nStarting new test case\n')

        """Put here functions that you want to run before every test case"""

    def test_first(self):
        test_name = ''
        """Write here your test, every new test should start as new fuction with name test_"""

    def tearDown(self):
        super().tearDown()
        self.bp.reset_app()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.bp.close_app()
        end_session(cls.driver)
