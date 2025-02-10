#from pyenv.tests.test_pyenv_feature_exec import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
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


greenplum_bi = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_greenplum")))
greenplum_bi.click()
time.sleep(1)

tabs = driver.window_handles
driver.switch_to.window(tabs[0])

time.sleep(2)
button_update = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='button button button_main button_update']")))
button_update.click()
time.sleep(2)
button_update.click()
button_update = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_nifi")))
