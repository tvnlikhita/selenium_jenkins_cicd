from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
browser.get("https://practice.expandtesting.com/dropdown")
# browser.maximize_window()

choose = Select(browser.find_element(By.ID, "dropdown"))
choose.select_by_visible_text("Option 1")

choose_country = Select(browser.find_element(By.ID, "country"))
choose_country.select_by_visible_text("India")

time.sleep(3)