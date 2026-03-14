from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()


websites = [
    "https://www.thesouledstore.com",
    "https://www.nike.com",
    "https://www.bbc.com",
    "https://www.python.org"
]

for site in websites:
    sleep(3)
    driver.get(site)

    sleep(3)

    print("Website:", site)
    print("Title:", driver.title)
    print("-------------------------")

driver.quit()