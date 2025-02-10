from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome(options=chrome_options)


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

options.add_argument("--start-maximized")
driver.get("https://hdak.nbrb.by/")

superset_bi = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_superset")))
superset_bi.click()
time.sleep(1)

tabs = driver.window_handles
#print(tabs)
driver.switch_to.window(tabs[1])

login_sso = driver.find_element(By.CSS_SELECTOR, "#userNameInput")
login_sso.send_keys("test_analitic_xdak@nbrb.by") #в AD роль Администратор
password_sso = driver.find_element(By.CSS_SELECTOR, "#passwordInput")
password_sso.send_keys('kcrrcTEj')
submit = driver.find_element(By.CSS_SELECTOR, "#submitButton")
submit.click()

menu_superset_available = WebDriverWait(driver, 100).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR,"[class = ant-card-body]")))
print(f'В суперсете отображается пунктов меню : {len(menu_superset_available)}')

time.sleep(2)

settings_dropdown_button = driver.find_element(By.CSS_SELECTOR, "span[class='anticon css-vdqyuj']")


actions = ActionChains(driver)
actions.move_to_element(settings_dropdown_button).perform()
time.sleep(2)


menu_item_profile = driver.find_element(By.CSS_SELECTOR, "ul li a[href='/profile/']")
menu_item_profile.click()

profile_role = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "p[class=roles]")))

role_text = profile_role.text

print(f'Роль Superset: {role_text}')

time.sleep(2)



time.sleep(2)

driver.switch_to.window(tabs[0])

datahub = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_datahub")))
datahub.click()
time.sleep(2)

tabs = driver.window_handles
#print(tabs)
driver.switch_to.window(tabs[2])
datahub_domains = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class = 'sc-iVCqfc gOzXug']"))).is_displayed()
print(f'страница Datahub отображается (каталоги) {str(datahub_domains)}')

menu__profile = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='manage-account-menu']")))
menu__profile.click()

your_profile_role = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul li:nth-child(3)")))
your_profile_role.click()
time.sleep(2)
role_datahub = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[class=ant-tag]")))
print(f'Роль Datahub:', role_datahub.text)

tabs = driver.window_handles
#print(tabs)
driver.switch_to.window(tabs[0])

nifi_ = WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_nifi")))
nifi_.click()
time.sleep(10)

tabs = driver.window_handles
#print(tabs)
driver.switch_to.window(tabs[3])
current_user_nifi = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#current-user")))
print(f'User in nifi: '+current_user_nifi.text)

process_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "g[id = canvas] g"))).is_displayed()
print(f'страница nifi отображается {str(process_menu)}')
#подсчитать количество тегов внутри $$('g[id = canvas] g')

tabs = driver.window_handles
#print(tabs)
driver.switch_to.window(tabs[0])

greenplum_ = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_greenplum")))
greenplum_.click()

tabs = driver.window_handles
#print(tabs)
driver.switch_to.window(tabs[4])


greenplum_ = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class=greenplum-discription__driver-link]"))).is_displayed()
print(f'страница greenplum отображается {str(greenplum_)}')
tabs = driver.window_handles
#print(tabs)
driver.switch_to.window(tabs[0])

users_control = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#systemLink_userset")))
users_control.click()


