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
driver.get("http://10.35.1.81:8081/")


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
input_user_login.send_keys('test_guest')

input_user_pass = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=password]")))
input_user_pass.send_keys('kcrrcTEj')

button_submit_log_in = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='button buton button_main form_logIn__button']")))
button_submit_log_in.click()
time.sleep(10)

superset_bi = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "ul li:nth-child(2) a")))
superset_bi.click()
time.sleep(10)

login = driver.find_element(By.CSS_SELECTOR, "#userNameInput")
login.send_keys("varchak_dv@nbrb.by")
password = driver.find_element(By.CSS_SELECTOR, "#passwordInput")
password.send_keys('8Var12Dim')
submit = driver.find_element(By.CSS_SELECTOR, "#submitButton")
submit.click()

# login_sso = driver.find_element((By.CSS_SELECTOR, "input[id=userNameInput]"))
# time.sleep(2)
#
# login_sso.send_keys("varchak_dv@nbrb.by")


# user = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr[id='1682'] a[href='/userset/editUser/1682']")))
# user.click()
# time.sleep(1)
# data_hub_viwe = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[id ='urn:li:dataHubGroup:View']")))
# data_hub_viwe.click()
# time.sleep(1)
# data_hub_viwe.click()
# time.sleep(10)