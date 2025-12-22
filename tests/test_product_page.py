import pytest
import time
from pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
      'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
      pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail(reason='problem with offer')),
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]




@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.price_and_name()
    page.press_button_add_to_chart()
    page.solve_quiz_and_get_code()
    page.is_price_and_name_ordered_presents()
    page.is_name_presents_correctly()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_chart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_chart()
    page.solve_quiz_and_get_code()
    page.should_dissapeare_succes_message()
