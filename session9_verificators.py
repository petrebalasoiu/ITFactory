from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# why all caps?
class Login(TestCase):
    FORM_AUTHENTICATION = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    TITLE = (By.XPATH, '//head/title')
    HEADER = (By.XPATH, '//*[@id="content"]/div/h2')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    ELEMENTAL_SELENIUM = (By.XPATH, '//a[contains(text(), "Elemental Selenium")]')
    LOGIN_ERROR = (By.XPATH, '//div/*[@id="flash"]')
    USERNAME = (By.XPATH, '//*[@id="username"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    DISMISS_ERROR = (By.XPATH, '//*[@id="flash"]/a')
    FLASH_SUCCESS = (By.XPATH, '//*[@class="flash success"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@class="button secondary radius"]')
    SUBHEADER = (By.XPATH, '//*[@class="subheader"]')

    # without variable 's'?
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.find_element(*self.FORM_AUTHENTICATION).click()

    def tearDown(self) -> None:
        self.driver.quit()

    # Test 1: Checks if the new url is correct
    def test_new_url(self):
        expected = 'https://the-internet.herokuapp.com/login'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'The new URL does not match')

    # Test 2: Checks if the page title is correct
    def test_page_title(self):
        expected = 'The Internet'
        actual = self.driver.title
        self.assertEqual(expected, actual, 'The page title does not match')

    # Test 3: Checks if the XPath element //h2 is correct
    def test_xpath_element(self):
        expected = self.driver.find_element(By.XPATH, '//h2')
        actual = self.driver.find_element(*self.HEADER)
        self.assertEqual(expected, actual, 'The XPath elements do not match')

    # Test 4: Checks if the login button is displayed
    def test_login_button(self):
        button = self.driver.find_element(*self.LOGIN_BUTTON)
        self.assertIsNotNone(button, 'The button is not displayed')

    # Test 5: Checks if the href atribute of 'Elemental Selenium' link is correct
    def test_href_link(self):
        expected = 'http://elementalselenium.com/'
        actual = self.driver.find_element(*self.ELEMENTAL_SELENIUM).get_attribute('href')
        self.assertEqual(expected, actual, 'The href link is not correct')

    # Test 6: Checks if the login error is displayed with no credentials typed (nu am inteles nimic din asta)
    def test_login_error_no_credentials(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        error = self.driver.find_element(*self.LOGIN_ERROR)
        self.assertIsNotNone(error, 'Is not displayed')

    # Test 7: Checks if the login error is displayed with invalid credentials
    def test_login_error_invalid_credentials(self):
        self.driver.find_element(*self.USERNAME).send_keys('bradd_pit')
        self.driver.find_element(*self.PASSWORD).send_keys('123456')
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        expected = 'Your username is invalid!'
        actual = self.driver.find_element(*self.LOGIN_ERROR).text
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    # Test 8: Checks if the login error gets dismissed successfully
    def test_login_error_dismissal(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.driver.find_element(*self.DISMISS_ERROR).click()
        error = self.driver.find_element(*self.LOGIN_ERROR)
        self.assertIsNotNone(error, 'The error was not dismissed')

    # Test 9: (INCORECT) Checks if the text label matches
    def test_labels_text(self):
        # The variables below are optional
        username_label = self.driver.find_element(*self.USERNAME).text
        password_label = self.driver.find_element(*self.PASSWORD).text
        labels = [username_label, password_label]
        expected = 'Username, Password'
        self.assertTrue(labels[0] in expected, 'Username not matching')
        self.assertTrue(labels[1] in expected, 'Password not matching')

    # Test 10: (INCOMPLET) Checks if the valid credentials take to a secure area
    def test_login_valid_credentials(self):
        self.driver.find_element(*self.USERNAME).send_keys('tomsmith')
        self.driver.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        # # varianta cu assertIsNotNone
        link = 'https://the-internet.herokuapp.com/secure'
        self.assertIsNotNone(link, 'test')
        # # varianta cu assertEqual
        expected = 'https://the-internet.herokuapp.com/secure'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'test')
        flash = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(self.FLASH_SUCCESS))
        self.assertIsNotNone(flash, 'The flash message is not displayed')
        expected = 'secure area!'
        self.assertTrue(expected in flash.text, 'The message is not displayed')

    # Test 11: Checks if the logout button redirects to the previous site after valid credentials
    def test_logout_button(self):
        self.driver.find_element(*self.USERNAME).send_keys('tomsmith')
        self.driver.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
        expected = 'https://the-internet.herokuapp.com/login'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'The website does not match')

    # Test 12: Checks if a brute force password hacking can crack the login
    def brute_force_password_hacking(self):
        self.driver.find_element(*self.USERNAME).send_keys('tomsmith')
        split_text = self.driver.find_element(*self.SUBHEADER).text.split(' ')
        password = 'SuperSecretPassword!'
        for word in split_text:
            self.driver.find_element(*self.PASSWORD).send_keys(word)
            if word == password:
                print(f'The secret password is {password}')
            else:
                print('The password could not be found')









