from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

options.add_argument("--start-maximized")
driver.get("https://hdak.nbrb.by/")


#убедиться, что страница открылась

manual_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button_manual")))
#manual_button.click()
#time.sleep(10)

#Управление пользоваелями
#user_set = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/userset']")))
#user_set.click()


#edit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//tr[td[contains(text(), 'nesterovich_yuyu')]]//i[contains(@class, 'icon-edit')]")))
#edit_button.click()