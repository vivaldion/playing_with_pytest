from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL =  (By.CSS_SELECTOR, "#login_link")
    login_form = (By.CSS_SELECTOR, '#login_form')
    register_form = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    add_to_chart = (By.CSS_SELECTOR, ".btn-add-to-basket")
    price_value = (By.CSS_SELECTOR, ".product_main p.price_color")
    product_name = (By.CSS_SELECTOR, '.product_main h1')
    price_value_ordered = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    product_name_ordered = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    success_added = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')