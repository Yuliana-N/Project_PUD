import driver
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)

def first_login():
    browser.get("http://10.35.1.81:8081/")
    time.sleep(5)

def logout():
    browser.find_element(By.CSS_SELECTOR, '.button_exit').click()




