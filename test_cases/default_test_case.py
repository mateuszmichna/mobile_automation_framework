import unittest

from pages.base_page import BasePage
from settings.session_settings import start_session, end_session


class BaseTestCaseSet(unittest.TestCase):
    basepage = None
    driver = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        """Here are functions that are run before all tests in this class (ex. initialization of driver and BasePage """

        cls.driver = start_session()
        cls.basepage = BasePage(driver=cls.driver)
        cls.basepage.print_screen_size()
        cls.basepage.print_screen_orientation()

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
        self.basepage.reset_app()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.basepage.close_app()
        end_session(cls.driver)
