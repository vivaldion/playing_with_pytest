from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*CartPageLocators.CART_TITLE, timeout=1), "Cart is not empty"
        assert self.is_element_present(*CartPageLocators.CART_INNER), "Wrong cart section"
        text_in_cart = self.browser.find_element(*CartPageLocators.CART_INNER).text
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        assert CartPageLocators.empty_text[language] in text_in_cart, "Empty cart text not found"