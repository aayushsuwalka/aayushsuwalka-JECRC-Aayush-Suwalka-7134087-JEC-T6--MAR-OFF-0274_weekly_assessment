# Task 3
# Open Google
# Enter "Selenium Python"
# Use explicit wait for suggestions
# Capture all suggestions using find_elements
# Print them
# Click one suggestion
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 15)
driver.get("https://www.google.com")
driver.maximize_window()
searchBar = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='APjFqb']")))
searchBar.send_keys("Selenium Python")
suggestions = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@role='listbox']//li//span")))
for i in suggestions:
    print(i.text)
clickItem=wait.until(EC.element_to_be_clickable((By.XPATH,'//ul[@role="listbox"]/child::li[4]')))
clickItem.click()
driver.quit()