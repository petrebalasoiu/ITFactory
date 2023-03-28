"""
Choose one or more websites from the list below
- https://www.phptravels.net/
- http://automationpractice.com/index.php
- https://formy-project.herokuapp.com/
- https://the-internet.herokuapp.com/
- https://www.techlistic.com/p/selenium-practice-form.html
- jules.app

Choose 3 of each type of selectors below:
● ID
● Link text
● Parțial link text
● Name
● Tag*
● Class name*
● Css (1 after ID, 1 after class, 1 after attribute=partial_value)
For XPath identify the elements by the attributes below:

● 3 after attribute value
● 3 after the element's text
● 1 after partial text
● 1 after pipe
● 1 with *
● 1 (xpath)[1]
● 1 using parent::
● 1 using preceding or following sibling
● 1 function that allows the user to choose through parameter the element to interact with
"""

# all necessary imports
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# initializing driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# accessing website
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
# driver.maximize_window()
sleep(2)

# element found By.ID (1)
cookies = driver.find_element(By.ID, 'ez-accept-all')
cookies.click()
sleep(2)

# clicking in a certain position based on coordinates
action = ActionChains(driver)
action.move_by_offset(50, 50).click().perform()
sleep(2)

# element found by TAG_NAME (1/3)
first_name = driver.find_elements(By.TAG_NAME, 'input')
first_name[0].send_keys('Petre')
sleep(1)

# element found by NAME (1/3)
first_name2 = driver.find_element(By.NAME, 'firstname')
first_name2.clear()
first_name2.send_keys('Pavel')
sleep(1)

# element found by TAG_NAME (2/3)
last_name = driver.find_elements(By.TAG_NAME, 'input')
last_name[1].send_keys('Balasoiu')
sleep(1)

# element found by NAME (2/3)
last_name2 = driver.find_element(By.NAME, 'lastname')
last_name2.clear()
last_name2.send_keys('Marin')
sleep(1)

# element found by TAG_NAME (3/3)
gender = driver.find_elements(By.TAG_NAME, 'input')
gender[2].click()
sleep(1)

# element found by ID (1/3)
experience = driver.find_element(By.ID, 'exp-1')
experience.click()
sleep(1)

# element found by ID (2/3)
date = driver.find_element(By.ID, 'datepicker')
date.send_keys('05/03/2023')
sleep(1)

# element found by ID (3/3)
profession = driver.find_element(By.ID, 'profession-1')
profession.click()
sleep(1)

# element found by NAME (3/3)
tool = driver.find_element(By.NAME, 'tool')
tool.click()
sleep(1)

# element found by XPATH (Extra)
continents2 = driver.find_element(By.XPATH, '//*[@id="continents"]/option[2]')
continents2.click()
sleep(1)

# element found by XPATH (Extra)
continents3 = driver.find_element(By.XPATH, '//*[@id="continents"]/option[3]')
continents3.click()
sleep(1)

# element found by XPATH (Extra)
selenium_commands = driver.find_element(By.XPATH, '//*[@id="selenium_commands"]/option[1]')
selenium_commands.click()
sleep(1)

# element found by LINK_TEXT (1/3)
link1 = driver.find_element(By.LINK_TEXT, 'Automate Amazon like E-Commerce website with Selenium')
link1.click()
sleep(1)
driver.back()

# element found by LINK_TEXT (2/3)
link2 = driver.find_element(By.LINK_TEXT, 'Automate GoDaddy website features with Selenium')
link2.click()
sleep(1)
driver.back()

# element found by LINK_TEXT (3/3)
link3 = driver.find_element(By.LINK_TEXT, 'Automate Google search with Selenium')
link3.click()
sleep(1)
driver.back()

# element found by PARTIAL_LINK_TEXT (1/3)
link4 = driver.find_element(By.PARTIAL_LINK_TEXT, 'How to Find')
link4.click()
sleep(1)
driver.back()

# element found by PARTIAL_LINK_TEXT (2/3)
link5 = driver.find_element(By.PARTIAL_LINK_TEXT, 'How to Handle')
link5.click()
sleep(1)
driver.back()

# element found by PARTIAL_LINK_TEXT (3/3)
link6 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Automate Handling')
link6.click()
sleep(1)
driver.back()

# accessing website
driver.get('https://phptravels.net/')
# driver.maximize_window()
sleep(2)

# element found by CSS_SELECTOR (1/3)
flights_tab = driver.find_element(By.CSS_SELECTOR, 'button#flights-tab')
flights_tab.click()
sleep(2)

# element found by CSS_SELECTOR (2/3)
two_way = driver.find_element(By.CSS_SELECTOR, 'input.form-check-input#round-trip')
two_way.click()
sleep(2)

# accessing website
driver.get('https://formy-project.herokuapp.com/autocomplete')
# driver.maximize_window()
sleep(1)

# element found by CSS_SELECTOR (3/3)
address = driver.find_element(By.CSS_SELECTOR, 'div input[placeholder*="address"]')
address.send_keys('1 Angel Street')
sleep(2)

# element found by CLASS_NAME (1/3)
city = driver.find_elements(By.CLASS_NAME, 'form-control')
city[3].send_keys('Anycity')
sleep(2)

# element found by CLASS_NAME (2/3)
state = driver.find_elements(By.CLASS_NAME, 'form-control')
state[4].send_keys('Anystate')
sleep(2)

# element found by CLASS_NAME (3/3)
country = driver.find_elements(By.CLASS_NAME, 'form-control')
country[6].send_keys('Anycountry')
sleep(2)

# accessing website
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.maximize_window()
sleep(2)

# # element found by ID (Extra)
cookies = driver.find_element(By.ID, 'ez-accept-all')
cookies.click()
sleep(2)

# clicking in a certain position based on coordinates
action = ActionChains(driver)
action.move_by_offset(200, 200).click().perform()
sleep(2)

# element found by XPATH (Extra)
firstname = driver.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input')
firstname.send_keys('Mircea')
sleep(2)

# element found by XPATH (Extra)
lastname = driver.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[5]/input')
lastname.send_keys('Stanescu')
sleep(2)

# element found by XPATH (*)
gender2 = driver.find_element(By.XPATH, '//*[@id="sex-0"]')
gender2.click()
sleep(2)

# element found by XPATH attribute-value (1/3)
yrs_of_exp = driver.find_element(By.XPATH, '//input[@id="exp-2"]')
yrs_of_exp.click()
sleep(2)

# element found by XPATH attribute-value (2/3)
datepicker = driver.find_element(By.XPATH, '//input[@id="datepicker"]')
datepicker.send_keys('05/03/2023')
sleep(2)

# element found by XPATH attribute-value (3/3)
profi = driver.find_element(By.XPATH, '//input[@id="profession-0"]')
profi.click()
sleep(2)

# element found by XPATH (Pipe)
t00l = driver.find_element(By.XPATH, '//input[@id="tool-0"] | //input[@id="tool-1"] | //input[@id="tool-2"]')
t00l.click()
sleep(2)

# element found by XPATH [1]
continetss2 = driver.find_element(By.XPATH, '//*[@id="continents"]/option[2]')
continetss2.click()
sleep(5)

# element found by XPATH text (1/3)
link_1 = driver.find_element(By.XPATH, '//a[text()="Automate Amazon like E-Commerce website with Selenium"]')
link_1.click()
sleep(2)
driver.back()

# element found by XPATH text (2/3)
link_2 = driver.find_element(By.XPATH, '//a[text()="Automate GoDaddy website features with Selenium"]')
link_2.click()
sleep(2)
driver.back()

# element found by XPATH text (3/3)
link_3 = driver.find_element(By.XPATH, '//a[text()="Automate Google search with Selenium"]')
link_3.click()
sleep(2)
driver.back()

# element found by XPATH partial text
link_4 = driver.find_element(By.XPATH, '//a[contains(text(), "How to Find")]')
link_4.click()
sleep(2)
driver.back()

# element found by XPATH parent
link_5 = driver.find_element(By.XPATH, '//a[text()="How to Handle Static and Dynamic Web table with Selenium"]/parent::li')
link_5.click()
sleep(2)

# accessing website
driver.get('https://formy-project.herokuapp.com/autocomplete')
# driver.maximize_window()
sleep(2)

# element found by XPATH following sibling
select_address = driver.find_element(By.XPATH, '//form//label[text()="Address"]/parent::*/following-sibling::input')
select_address.send_keys('Adresa')
sleep(2)


# function with parameters used to find the element
def full_address(label, input_value):
    my_input = driver.find_element(By.XPATH, f'//label[text()="{label}"]/parent::strong/parent::div//input')
    my_input.send_keys(input_value)


full_address('Address', 'Str. 1 Decembrie')
full_address('City', 'Mangalia')
full_address('Country', 'Romania')
sleep(5)
