from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://xdsuperset.nbrb.by/login/")

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

# Вводим учетные данные
username_input.send_keys("varchak_dv")
password_input.send_keys("8Var12Dim")
password_input.send_keys(Keys.RETURN)
driver.get('https://xdsuperset.nbrb.by/roles/show/1')

elem = driver.find_element(By.CSS_SELECTOR, "#Home tr:nth-child(2) td")

per_sup_list =[]
#setings = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ant-menu-submenu.ant-menu-submenu-horizontal.css-d1dar4")))
for i in elem.text.replace('[', '').replace(']', '').split(', '):
    per_sup_list.append(i)
time.sleep(2)
print(len(per_sup_list))


driver.get("https://superset.nbrb.by/roles/show/186")
login = driver.find_element(By.CSS_SELECTOR, "#userNameInput")
login.send_keys("varchak_dv@nbrb.by")
password = driver.find_element(By.CSS_SELECTOR, "#passwordInput")
password.send_keys('8Var12Dim')
submit = driver.find_element(By.CSS_SELECTOR, "#submitButton")
submit.click()
time.sleep(15)
driver.get('https://superset.nbrb.by/roles/show/186')

elem = driver.find_element(By.CSS_SELECTOR, "#Home tr:nth-child(2) td")

per_sup_test_list =[]
#setings = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.ant-menu-submenu.ant-menu-submenu-horizontal.css-d1dar4")))
for i in elem.text.replace('[', '').replace(']', '').split(', '):
    per_sup_test_list.append(i)

time.sleep(2)
print(len(per_sup_test_list))

time.sleep(6)