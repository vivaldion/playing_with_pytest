from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def test_add_to_chart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    try:
        button_add_to_chart = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form button.btn[type='submit']")
        time.sleep(5)
        print('button founded')
        assert button_add_to_chart.is_enabled(), "Button is inactive"
    except NoSuchElementException as e:
        raise AssertionError(f"Element button was not found. Error: {str(e)}")