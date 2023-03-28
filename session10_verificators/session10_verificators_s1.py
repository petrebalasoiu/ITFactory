""" This is the first test suite """

from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


class TopHUD(TestCase):

    MY_ACCOUNT = (By.XPATH, '//*[@id="my_account"]')
    MY_WISHLIST = (By.XPATH, '//*[@id="my_wishlist"]')
    MY_CART = (By.XPATH, '//*[@id="my_cart"]')
    SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
    SEARCH_BOX_SUBMIT = (By.XPATH, '//button[@class="btn btn-default searchbox-submit-button"]')
    HOME_BUTTON = (By.XPATH, '//*[@class="navbar-brand"]')

    def setUp(self) -> None:
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.emag.ro/')

    def tearDown(self) -> None:
        self.driver.quit()

    def test_my_account(self):
        self.driver.find_element(*self.MY_ACCOUNT).click()
        expected = 'https://auth.emag.ro/user/login'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'My account link does not match')

    def test_my_wishlist(self):
        self.driver.find_element(*self.MY_WISHLIST).click()
        expected = 'https://www.emag.ro/favorites?ref=ua_favorites'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'My wishlist link does not match')

    def test_my_cart(self):
        self.driver.find_element(*self.MY_CART).click()
        expected = 'https://www.emag.ro/cart/products?ref=cart'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'My cart link does not match')

    def test_search_box(self):
        self.driver.find_element(*self.SEARCH_BOX).send_keys('detergent')
        self.driver.find_element(*self.SEARCH_BOX_SUBMIT).click()
        expected = 'https://www.emag.ro/search/detergent?ref=effective_search'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'The search box link does not match')

    def test_home_button(self):
        self.driver.find_element(*self.HOME_BUTTON).click()
        expected = 'https://www.emag.ro/'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'The home button does not function')



