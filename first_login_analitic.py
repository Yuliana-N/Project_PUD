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

#Управление пользоваелями
user_set = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/userset']")))
#user_set.click()
#time.sleep(10)

log_out_button = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button_exit")))
log_out_button.click()

input_user_login = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=userLogin]")))
input_user_login.send_keys('test_hdak3')

input_user_pass = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=password]")))
input_user_pass.send_keys('kcrrcTEj')

button_submit_log_in = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='button buton button_main form_logIn__button']")))
button_submit_log_in.click()
time.sleep(10)

superset_bi = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_superset")))
superset_bi.click()
time.sleep(1)

tabs = driver.window_handles
driver.switch_to.window(tabs[1])

login_sso = driver.find_element(By.CSS_SELECTOR, "#userNameInput")
login_sso.send_keys("test_hdak3@nbrb.by")
password_sso = driver.find_element(By.CSS_SELECTOR, "#passwordInput")
password_sso.send_keys('kcrrcTEj')
submit = driver.find_element(By.CSS_SELECTOR, "#submitButton")
submit.click()

time.sleep(2)

settings_dropdown_button = driver.find_element(By.CSS_SELECTOR, "span [class = 'anticon css-vdqyuj']")

actions = ActionChains(driver)
actions.move_to_element(settings_dropdown_button).perform()
time.sleep(2)


menu_item_profile = driver.find_element(By.CSS_SELECTOR, "ul li a[href='/profile/']")
menu_item_profile.click()


# login_sso = driver.find_element((By.CSS_SELECTOR, "input[id=userNameInput]"))
# time.sleep(2)
#
# login_sso.send_keys("@nbrb.by")


# user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr[id='1682'] a[href='/userset/editUser/1682']")))
# user.click()
# time.sleep(1)
# data_hub_viwe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id ='urn:li:dataHubGroup:View']")))
# data_hub_viwe.click()
# time.sleep(1)
# data_hub_viwe.click()
# time.sleep(10)