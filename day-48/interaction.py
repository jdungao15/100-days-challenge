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


# store all product in a list

product_store = []

for i in range(19):
    try:
        product = driver.find_element(By.ID, f"product{i}")
        product_store.append(product)
    except NoSuchElementException:
        product = driver.find_element(By.ID, f"product{i}")

product_store.reverse()
while True:
    cookies_text = driver.find_element(By.ID, "cookies").text.split("per second: ")[0]
    cookies_amount = int(cookies_text.split("cookie")[0])

    try:
        cookie.click()
    except StaleElementReferenceException:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
    for product in product_store:
        try:
            # check if product is displayed on the page
            if product.is_displayed():
                product_price = product.find_element(By.CLASS_NAME, "price").text
                print(cookies_amount)
                # check if the user cookies is greater than the product price
                if cookies_amount > float(product_price.replace(',', "")):
                    product.click()
        except StaleElementReferenceException:
            pass
