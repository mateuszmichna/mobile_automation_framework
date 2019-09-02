from pages.base_page import BasePage


class ApiDemosPage(BasePage):

    """Selectors with possible actions"""
    views_button = 'Views'  # access_Id
    text_fields_button = 'TextFields'  # access_id
    txt_field = '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText'  #xpath

    """Element actions"""

    def tap_views(self):
        views = self.find_element_by_access_id(self.views_button)
        self.tap_on_element_wda(views)

    def tap_Text_Fields(self):
        textfields = self.find_element_by_access_id(self.text_fields_button)
        self.tap_on_element_wda(textfields)

    def tap_txt_field(self):
        txtfields = self.find_element_by_xpath(self.txt_field)
        self.tap_on_element_wda(txtfields)

    def send_keys_to_txt_field(self, keys: str):
        self.send_keys_wda(keys, self.txt_field, 'xpath')

    def clear_txt_field(self):
        self.clear_field_wda(self.txt_field, 'xpath')
