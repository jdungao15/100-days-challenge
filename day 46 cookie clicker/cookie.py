from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Cookie:

    def __init__(self):
        self.timeout = time.time() + 30
        self.five_min = time.time() + 60 * 5  # 5minutes
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        self.product_store = []
        self.start_click = False

        # wait until browser load up
        time.sleep(5)

        language_en = self.driver.find_element(By.ID, "langSelect-EN")
        language_en.click()
        cookie = self.driver.find_element(By.ID, "bigCookie")

        time.sleep(3)
        self.get_all_products()

    def go_to_options(self):
        options = self.driver.find_element(By.ID, "prefsButton").find_element(By.CLASS_NAME, "subButton")
        options.click()

    def save_file(self):
        if self.start_click:
            self.start_click = False
        else:
            self.go_to_options()
            time.sleep(2)
            export_save = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[1]")
            export_save.click()
            data = self.driver.find_element(By.ID, "textareaPrompt")
            with open("cookies_data.txt", "w") as f:
                f.write(data.text)
            all_done_button = self.driver.find_element(By.ID,"promptOption0")
            all_done_button.click()
            time.sleep(1)
            exit_button = self.driver.find_element(By.CLASS_NAME, "menuClose")
            exit_button.click()

    def convert_to_cookies_amount(self, c_amount):

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

    def upload_data(self):
        if self.start_click:
            self.start_click = False
            self.main()
        else:
            self.go_to_options()
            import_save = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[2]")
            import_save.click()
            text_area = self.driver.find_element(By.ID, "textareaPrompt")
            with open("cookies_data.txt", "r") as f:
                data = f.read()
                text_area.send_keys(data)
                load = self.driver.find_element(By.ID, "promptOption0")
                load.click()
                time.sleep(3)
                close = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[18]/div[2]/div[4]/div[1]")
                close.click()

    def get_all_products(self):
        for i in range(19):
            try:
                product = self.driver.find_element(By.ID, f"product{i}")
                self.product_store.append(product)
            except NoSuchElementException:
                product = self.driver.find_element(By.ID, f"product{i}")
        self.product_store.reverse()

    def main(self):
        while self.start_click:
            cookie = self.driver.find_element(By.ID, "bigCookie")
            cookie.click()
            cookies_text = self.driver.find_element(By.ID, "cookies").text.split("per second: ")[0]
            cookies_amount = float(self.convert_to_cookies_amount(cookies_text))

            # Wait five seconds
            if time.time() > self.timeout:
                for product in self.product_store:
                    try:
                        # check if product is displayed on the page
                        if product.is_displayed() and product.is_enabled():
                            product_price = product.find_element(By.CLASS_NAME, "price").text
                            # check if the user cookies is greater than the product price
                            if cookies_amount > float(self.convert_to_cookies_amount(product_price)):
                                product.click()
                    except ElementClickInterceptedException:
                        pass
                self.timeout = time.time() + 5

            try:
                golden_cookie = self.driver.find_element(By.ID, "goldenCookie")
                golden_cookie.click()
            except ElementNotInteractableException:
                pass
    def start(self):
        self.start_click = True
        self.main()
    def stop(self):
        self.start_click = False
        self.main()


