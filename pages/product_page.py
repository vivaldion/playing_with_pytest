from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.button_add_to_chart = None
        #self.button_add_to_chart = self.browser.find_element(*ProductPageLocators.add_to_chart)

    def should_be_add_to_chart_button(self):
        assert self.is_element_present(*ProductPageLocators.add_to_chart),\
            "Add to chart button is not presented"

        self.button_add_to_chart = self.browser.find_element(*ProductPageLocators.add_to_chart)
        return True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.success_added), \
            "Success message is presented, but should not be"

    def should_dissapeare_succes_message(self):
        assert self.is_disappeared(*ProductPageLocators.success_added), \
        'should disspeare, but didnt'

    def press_button_add_to_chart(self):
        if self.button_add_to_chart is None:
            self.should_be_add_to_chart_button()
        self.button_add_to_chart.click()

    def is_price_and_name_ordered_presents(self):
        self.is_price_presents_ordered()
        self.is_name_presents_ordered()


    def price_and_name(self):
        try:
            self.name = self.browser.find_element(*ProductPageLocators.product_name).text
            self.price = self.browser.find_element(*ProductPageLocators.price_value).text
        except NoSuchElementException:
            raise AssertionError('There is no name in price or product page')


    def is_price_presents_ordered(self):
        self.is_element_present(*ProductPageLocators.price_value_ordered)
        self.price_ordered = self.browser.find_element(*ProductPageLocators.price_value_ordered).text

    def is_name_presents_ordered(self):
        self.is_element_present(*ProductPageLocators.product_name_ordered)
        self.name_ordered = self.browser.find_element(*ProductPageLocators.product_name_ordered).text



    def is_name_presents_correctly(self):
        assert self.name == self.name_ordered, 'name is not correct'
        assert self.price == self.price_ordered, 'price is not correct'



