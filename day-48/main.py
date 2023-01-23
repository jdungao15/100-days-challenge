from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pprint as pp

chrome_driver_path = 'C:/Users/johnm/OneDrive/Documents/chromedriver_win32/chromedriver.exe'


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
s = Service(chrome_driver_path)
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://www.python.org/")

event_tags = driver.find_element(By.CSS_SELECTOR, ".event-widget .menu")

event_time_tag = [event_time.text for event_time in event_tags.find_elements(By.TAG_NAME, "time")]
event_name = [event.text for event in event_tags.find_elements(By.TAG_NAME, "a")]

events = dict(zip(event_time_tag, event_name))
pp.pprint(events)

driver.quit()
