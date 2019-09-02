from pages.base_page import BasePage


class KeyboardPage(BasePage):
    """Selectors with possible actions"""

    one_keyboard_button = ''  # accessibility id; tap
    two_keyboard_button = ''  # accessibility id; tap
    three_keyboard_button = ''  # accessibility id; tap
    four_keyboard_button = ''  # accessibility id; tap
    five_keyboard_button = ''  # accessibility id; tap
    six_keyboard_button = ''  # accessibility id; tap
    seven_keyboard_button = ''  # accessibility id; tap
    eight_keyboard_button = ''  # accessibility id; tap
    nine_keyboard_button = ''  # accessibility id; tap
    zero_keyboard_button = ''  # accessibility id; tap
    backspace_keyboard_button = ''  # accessibility id; tap

    """Element actions"""

    def tap_keyboard_button(self, which_button_selector: str):
        button = self.find_element_by_access_id(which_button_selector)
        return self.tap_on_element_wda(element=button)

    def tap_one_keyboard_button(self):
        return self.tap_keyboard_button(self.one_keyboard_button)

    def tap_two_keyboard_button(self):
        return self.tap_keyboard_button(self.two_keyboard_button)

    def tap_three_keyboard_button(self):
        return self.tap_keyboard_button(self.three_keyboard_button)

    def tap_four_keyboard_button(self):
        return self.tap_keyboard_button(self.four_keyboard_button)

    def tap_five_keyboard_button(self):
        return self.tap_keyboard_button(self.five_keyboard_button)

    def tap_six_keyboard_button(self):
        return self.tap_keyboard_button(self.six_keyboard_button)

    def tap_seven_keyboard_button(self):
        return self.tap_keyboard_button(self.seven_keyboard_button)

    def tap_eight_keyboard_button(self):
        return self.tap_keyboard_button(self.eight_keyboard_button)

    def tap_nine_keyboard_button(self):
        return self.tap_keyboard_button(self.nine_keyboard_button)

    def tap_zero_keyboard_button(self):
        return self.tap_keyboard_button(self.zero_keyboard_button)

    def tap_backspace_keyboard_button(self):
        return self.tap_keyboard_button(self.backspace_keyboard_button)

    def pick_phone_number(self, phone_number: str):
        functions = {'0': self.tap_zero_keyboard_button,
                     '1': self.tap_one_keyboard_button,
                     '2': self.tap_two_keyboard_button,
                     '3': self.tap_three_keyboard_button,
                     '4': self.tap_four_keyboard_button,
                     '5': self.tap_five_keyboard_button,
                     '6': self.tap_six_keyboard_button,
                     '7': self.tap_seven_keyboard_button,
                     '8': self.tap_eight_keyboard_button,
                     '9': self.tap_nine_keyboard_button}
        for a in phone_number:
            functions[a]()





