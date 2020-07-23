import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(executable_path=Path.cwd() / "chromedriver",)
driver.get('https://www.buzzfeed.com/')
time.sleep(3)
tasty = driver.find_element_by_link_text('Tasty')
print(tasty)
tasty.click()

