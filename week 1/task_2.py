from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org/")
driver.maximize_window()

sleep(2)

search_box = driver.find_element(By.ID, "searchInput")
print("Search field found:", search_box)

english_lang = driver.find_element(By.ID, "js-link-box-en")
print("English language found:", english_lang)

logo = driver.find_element(By.CLASS_NAME, "central-featured-logo")
print("Logo found:", logo)

languages = driver.find_elements(By.CSS_SELECTOR, ".central-featured-lang")
print("Number of language links:", len(languages))

english_lang.click()

sleep(2)

driver.back()
sleep(2)

driver.forward()
sleep(2)

driver.refresh()

print("Final Page Title:", driver.title)

driver.quit()