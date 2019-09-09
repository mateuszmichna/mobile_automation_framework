from pages.base_page import BasePage


class DefaultPage(BasePage):

    """Selectors with possible actions"""

    element_selector = ''  # accessibility id or xpath; possible action ex. tap

    """Element actions - tap"""

    def possible_action_tap(self):
        element = self.find_element_by_access_id(self.element_selector)
        self.tap_on_element_wda(element)

    """Element actions - send keys"""

    def send_keys_to_text_field_1(self, keys: str):
        element = self.find_element_by_access_id(self.element_selector)
        self.send_keys_wda(keys, element)

    """Element actions - clear fields"""

    def clear_text_field_1(self):
        element = self.find_element_by_access_id(self.element_selector)
        self.clear_field_wda(element)

    """Element actions - drag and drop"""

    def drag_element_to_x_y(self, to_x: int, to_y: int):
        drag_start = self.find_element_by_access_id(self.element_selector)
        self.drag_and_drop(element_1=drag_start, to_x=to_x, to_y=to_y)
        return drag_start



