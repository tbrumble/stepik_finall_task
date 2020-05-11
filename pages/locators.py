from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = '#content_inner > div > div.col-sm-6.login_form'
    REGISTER_FROM = '#content_inner > div > div.col-sm-6.register_form'
