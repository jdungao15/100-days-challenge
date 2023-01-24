from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pprint as pp

timeout = time.time() + 10
five_min = time.time() + 60 * 5  # 5minutes

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
driver.get("https://orteil.dashnet.org/cookieclicker/")

# wait until browser load up
time.sleep(5)

language_en = driver.find_element(By.ID, "langSelect-EN")
language_en.click()
cookie = driver.find_element(By.ID, "bigCookie")

time.sleep(3)


def go_to_options():
    options = driver.find_element(By.ID, "prefsButton").find_element(By.CLASS_NAME, "subButton")
    options.click()


def save_file():
    go_to_options()
    export_save = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[1]")
    export_save.click()
    data = driver.find_element(By.ID, "textareaPrompt")
    with open("cookies_data.txt", "w") as f:
        f.write(data.text)


def convert_to_cookies_amount(c_amount):
    cookie_currency = c_amount.replace("\n", "")
    currency_cookies = ["million cookies", "billion cookies", "trillion cookies",
                        "quadrillion cookies",
                        "quintillion cookies", "sextillion cookies", "septillion cookies"]
    upgrade_currency = [" million", " billion", " trillion", " quadrillion", " quintillion", " sextillion",
                        " septillion"]
    for currency in currency_cookies:
        if currency in cookie_currency:
            cookie_currency = float(cookie_currency.replace(currency, ""))
            return cookie_currency
            break
    for c in upgrade_currency:
        if c in cookie_currency:
            cookie_currency = float(c_amount.replace(c, ""))
            return float(cookie_currency)
            break

    if "," in cookie_currency:
        cookie_currency = c_amount.replace(",", "")
    elif "cookie\n" in c_amount:
        cookie_currency = c_amount.replace("cookie\n", "")
    elif "cookies\n" in c_amount:
        cookie_currency = float(c_amount.replace("cookies\n", ""))
    return cookie_currency


def upload_data():
    go_to_options()
    import_save = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[2]")
    import_save.click()
    text_area = driver.find_element(By.ID, "textareaPrompt")
    with open("cookies_data.txt", "r") as f:
        data = f.read()
        text_area.send_keys(data)
        load = driver.find_element(By.ID, "promptOption0")
        load.click()
        time.sleep(3)
        close = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[1]")
        close.click()


product_store = []
for i in range(19):
    try:
        product = driver.find_element(By.ID, f"product{i}")
        product_store.append(product)
    except NoSuchElementException:
        product = driver.find_element(By.ID, f"product{i}")

product_store.reverse()
upload_data()
while True:
    try:
        while True:
            cookie.click()
            cookies_text = driver.find_element(By.ID, "cookies").text.split("per second: ")[0]
            cookies_amount = float(convert_to_cookies_amount(cookies_text))

            #Wait five seconds
            if time.time()> timeout:
                for product in product_store:
                    try:
                        # check if product is displayed on the page
                        if product.is_displayed() and product.is_enabled():
                            product_price = product.find_element(By.CLASS_NAME, "price").text
                            # check if the user cookies is greater than the product price
                            if cookies_amount > convert_to_cookies_amount(product_price):
                                product.click()
                    except ElementClickInterceptedException:
                        pass
                timeout = time.time() + 5
    except StaleElementReferenceException:
        cookie = driver.find_element(By.ID, "bigCookie")
        cookie.click()
