# Task 1
# Automation script for amazon.com
# Open Amazon
# Verify page title and current URL
# Locate the category dropdown (next to search bar)
# Select "Books" using Select class
# Enter "Harry Potter" in search and press Enter
# Use explicit wait to wait until results are visible
# Get all product titles using find_elements
# Print first 5 product names
# Click on the first product
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
driver.get("https://amazon.in")
print(f'Driver Tittle : {driver.title}')
print(f'Driver Url : {driver.current_url}')
print(f'Driver Name : {driver.name}')
wait = WebDriverWait(driver, 10)
click_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'searchDropdownBox')))
sleep(2)
s = Select(click_dropdown)
s.select_by_value('search-alias=stripbooks')
sleep(2)
click_search =wait.until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
click_search.send_keys('Harry Potter')
click_search.send_keys(Keys.ENTER)
book_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']//h2//span")))
for book in book_list[:5]:
    print(book.text)
book_list[0].click()
sleep(3)
driver.quit()


