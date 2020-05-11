import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage:
    @pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/"])
    def test_purchases_button_is_exists_and_work(self, browser, link):

        try:
            print("\nopen link: " + link)
            browser.get(link)
            print("\nsleep")
            time.sleep(30)
            print("\nget button")
            login_link = browser.find_element_by_css_selector("#login_link")
            login_link.click()
        finally:
            print("\nend test_button_is_exists..")
            time.sleep(10)
