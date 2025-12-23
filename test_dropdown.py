from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get("https://practice.expandtesting.com/dropdown")
browser.maximize_window()

choose = Select(browser.find_element(By.ID, "dropdown"))
choose.select_by_visible_text("Option 1")

choose_country = Select(browser.find_element(By.ID, "country"))
choose_country.select_by_visible_text("India")

time.sleep(3)