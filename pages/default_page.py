from pages.base_page import BasePage


class DefaultPage(BasePage):

    """Selectors with possible actions"""

    element_selector = ''  # accessibility id or xpath; possible action ex. tap

    """Element actions"""

    def possible_action_tap(self):
        element = self.find_element_by_access_id(self.element_selector)
        self.tap_on_element_wda(element)



