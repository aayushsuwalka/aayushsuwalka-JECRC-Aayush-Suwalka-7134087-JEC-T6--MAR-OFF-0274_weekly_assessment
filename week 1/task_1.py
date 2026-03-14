from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()

sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
print("Username field:", username)

password = driver.find_element(By.CSS_SELECTOR, "input#password")
print("Password field:", password)

login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print("Login button:", login_button)

footer_link = driver.find_element(By.CSS_SELECTOR, "#page-footer a")
print("Footer link:", footer_link.text)

sleep(5)
driver.quit()