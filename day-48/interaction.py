from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pprint as pp

upgrade_items = []

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")

# wait until browser load up
time.sleep(5)

language_en = driver.find_element(By.ID, "langSelect-EN")
language_en.click()
cookie = driver.find_element(By.ID, "bigCookie")
# Get cookies amount
cookies_amount = float(driver.find_element(By.ID, "cookies").text[0])




# store all product in a list

for i in range(2):
    try:
        product = driver.find_element(By.ID, f"productPrice{i}")
        upgrade_items.append(product)
    except NoSuchElementException:
        continue

upgrade_items.reverse()

time.sleep(3)
cookie = driver.find_element(By.ID, "bigCookie")
# Get cookies amount
cookies_amount = float(driver.find_element(By.ID, "cookies").text[0])
# while True:
#     cookie.click()
#     for upgrade in upgrade_items:
#         try:
#             if cookies_amount > int(upgrade.text):
#                 print(upgrade.text)
#                 upgrade.click()
#         except StaleElementReferenceException:
#             continue



