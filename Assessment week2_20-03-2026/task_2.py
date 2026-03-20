# Task 2
# https://automationexercise.com/signup
# Open signup page
# Enter name & email
# Select Title (Mr/Mrs) → Radio button
# Select checkboxes:
# Newsletter
# Special offers
# Use get_attribute("checked") to verify selection


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opts)
wait = WebDriverWait(driver, 15)
driver.get('https://automationexercise.com/signup')
driver.maximize_window()
name = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
name.click()
name.send_keys("Aayush Suwalka")
email = driver.find_element(By.XPATH, "(//form[@action='/signup']/descendant::input)[3]")
email.click()
email.send_keys("aayush.suwalka08@gmail.com")
submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//form[@action='/signup']/descendant::button")))
submit_btn.click()
title_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='clearfix']/descendant::input")))
title_radio.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='newsletter']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='optin']"))).click()
newsletter = driver.find_element(By.ID, "newsletter")
print("Selected Newsletter:", newsletter.get_attribute("checked"))
offers = driver.find_element(By.ID, "optin")
print("Special offers :", offers.get_attribute("checked"))