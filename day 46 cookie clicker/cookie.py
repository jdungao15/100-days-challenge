from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class Cookie:

    def __init__(self):
        self.timeout = time.time() + 60 * 10  # 10 minutes
        self.five_min = time.time() + 60 * 5  # 5 minutes
        self.every_three_minutes = time.time() + 3 * 60  # 15 minutes
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")
        self.product_store = []
        self.start_click = False
        self.new_cookie_currency = ""

        # wait until browser load up
        time.sleep(5)

        language_en = self.driver.find_element(By.ID, "langSelect-EN")
        language_en.click()

        time.sleep(3)
        self.get_all_products()

    def upgrade_tool(self):
        # check if start_click is True, if yes, makes it false, then run upgrade_tool again
        if self.start_click:
            self.start_click = False
            self.upgrade_tool()
        else:
            try:
                # check if upgrade tool exist, if not pass
                tool = self.driver.find_element(By.ID, "upgrades").find_element(By.ID, "upgrade0")
                # if it exists click on upgrade tool
                if tool.is_displayed() and tool.is_enabled():
                    tool.click()
                    print("Tool Upgrade")
                    self.start()
                # if not return start click again
            except NoSuchElementException:
                self.start()

    def go_to_options(self):
        options = self.driver.find_element(By.ID, "prefsButton").find_element(By.CLASS_NAME, "subButton")
        options.click()

    def save_file(self):
        self.stop()
        self.go_to_options()
        time.sleep(2)
        try:
            export_save = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[2]/div[18]/div[2]/"
                                                   "div[4]/div[3]/div/div[4]/a[1]")
            export_save.click()
            data = self.driver.find_element(By.ID, "textareaPrompt")
            with open("cookies_data.txt", "w") as f:
                f.write(data.text)
            all_done_button = self.driver.find_element(By.ID, "promptOption0")
            all_done_button.click()
            time.sleep(2)
            self.go_to_options()
            print(f"File Saved {time.ctime(time.time())}")
            self.start()
        except NoSuchElementException:
            pass

    def convert_to_cookies_amount(self, c_amount):

        cookie_currency = c_amount.replace("\n", "").replace("cookies", "")
        upgrade_currency = ["million", "billion", "trillion", "quadrillion", "quintillion", "sextillion",
                            "septillion", "octillion", "nonillion", "undecillion", "duodecillion", 'tredecillion',
                            'quattuordecillion', 'quindecillion','sexdecillion','septendecillion' "decillion"]

        for c in upgrade_currency:
            if c in cookie_currency:
                new_cookie_currency = cookie_currency.replace(c, "")
                return float(new_cookie_currency)

        if "," in cookie_currency:
            self.new_cookie_currency = cookie_currency.replace(",", "")
        elif "cookie" in cookie_currency:
            self.new_cookie_currency = cookie_currency.replace("cookie", "")

        return float(self.new_cookie_currency)

    def has_same_units(self, product_v):
        upgrade_currency = ["million", "billion", "trillion", "quadrillion", "quintillion", "sextillion",
                            "septillion", "octillion", "nonillion", "undecillion", "duodecillion", 'tredecillion',
                            'quattuordecillion','quindecillion', 'sexdecillion','septendecillion', "decillion"]

        user_cookies = self.driver.find_element(By.ID, "cookies").text.split("per second: ")[0]
        product_price = product_v.find_element(By.CLASS_NAME, "price").text

        for c in upgrade_currency:
            if c in user_cookies and c in product_price:
                return True
        return False

    def pop_wrinkler(self):
        wrinkler = self.driver.execute_script("return document.querySelector('specialPopup')")
        wrinkler.execute_script("arguments[0].click();", wrinkler)

    def user_has_bigger_units(self, product):
        cookies_text = self.driver.find_element(By.ID, "cookies").text.split("per second: ")[0]
        product_price = product.find_element(By.CLASS_NAME, "price").text

        user_currency = cookies_text.replace("\n", "").replace("cookies", "")
        product_v = product_price.replace("\n", "").replace("cookies", "")
        units = {
            "septendecillion": 17,
            "sexdecillion": 16,
            'quindecillion': 15,
            'quattuordecillion': 14,
            'tredecillion': 13,
            "duodecillion": 12,
            'undecillion': 11,
            'decillion': 10,
            'nonillion': 9,
            "octillion": 8,
            "septillion": 7,
            "sextillion": 6,
            "quintillion": 5,
            "quadrillion": 4,
            "trillion": 3,
            "billion": 2,
            "million": 1,
            ",": 0,

        }
        # User Currency
        for key, val in units.items():
            if key in user_currency:
                user_currency = val
                break

        # Product Value
        for key, val in units.items():
            if key in product_v:
                product_v = val
                break

        if user_currency > product_v:
            return True
        else:
            return False

    def upload_data(self):
        if self.start_click:
            self.start_click = False
            self.main()
        else:
            self.go_to_options()
            import_save = self.driver.find_element(By.XPATH,
                                                   "/html/body/div[2]/div[2]/div[18]/div"
                                                   "[2]/div[4]/div[3]/div/div[4]/a[2]")
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
                print(f"File Uploaded {time.ctime(time.time())}")

    def get_all_products(self):
        for i in range(19):
            try:
                product = self.driver.find_element(By.ID, f"product{i}")
                self.product_store.append(product)
            except NoSuchElementException:
                pass
        self.product_store.reverse()

    def get_cookies_amount(self):
        cookies_text = self.driver.find_element(By.ID, "cookies").text.split("per second: ")[0]
        cookies_amount = float(self.convert_to_cookies_amount(cookies_text))
        return cookies_amount

    def get_product_price(self, product):
        product_price = product.find_element(By.CLASS_NAME, "price").text
        cookie_price = self.convert_to_cookies_amount(product_price)
        return cookie_price

    def main(self):
        while self.start_click:
            cookie = self.driver.find_element(By.ID, "bigCookie")
            cookie.click()
            # Wait 15 minutes
            if time.time() > self.timeout:

                for product in self.product_store:
                    affordable_products = True
                    # check if product is displayed on the page
                    if product.get_attribute("class") == "product unlocked enabled" \
                            and product.is_displayed() and product.is_enabled():
                        print(f"Available Product: {product.text}")

                        while affordable_products:
                            # check if user cookies have the same units as the product ex billions, millions
                            if self.has_same_units(product):
                                # check if user has enough cookies to buy the product
                                if self.get_cookies_amount() > self.get_product_price(product):
                                    try:
                                        product.click()
                                    except ElementClickInterceptedException:
                                        affordable_products = False
                                else:
                                    print(f"Not enough cookies for {product.text}")
                                    affordable_products = False
                            else:
                                # check if user has bigger units than the product ex billions, millions
                                if self.user_has_bigger_units(product):
                                    try:
                                        product.click()
                                    except ElementClickInterceptedException:
                                        affordable_products = False
                                else:
                                    print(f"Not enough cookies for {product.text}")
                                    affordable_products = False

                # add 10 seconds to 15 minutes
                self.timeout = time.time() + 60 * 60

            try:
                golden_cookie = self.driver.find_element(By.CLASS_NAME, "shimmer")
                if golden_cookie.is_displayed() and golden_cookie.is_enabled():
                    try:
                        golden_cookie.click()
                        print("Golden Cookie Click")
                    except StaleElementReferenceException:
                        raise ValueError("Golden Cookie Stale")
            except NoSuchElementException:
                pass
            except ElementClickInterceptedException:
                pass
            except StaleElementReferenceException:
                pass

            # Autosave every 5 minutes
            # if time.time() > self.five_min:
            #     self.five_min = time.time() + 60 * 30
            #     self.save_file()
            # Upgrade tools every 3 minutes
            # elif time.time() > self.every_three_minutes:
            #     self.every_three_minutes = time.time() + 60 * 3
            #     self.upgrade_tool()

    def start(self):
        self.start_click = True
        self.main()

    def stop(self):
        self.start_click = False
        self.main()
