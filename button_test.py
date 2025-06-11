from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ChromeDriver için Service nesnesini oluşturup path belirliyoruz.
service = Service(executable_path="chromedriver/chromedriver.exe") 

driver = webdriver.Chrome(service=service)

driver.get("https://reqres.in")

# 1. users butonuna tıklama
users_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="users"]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", users_button)
users_button.click()
time.sleep(2)  

# 2. users-single butonuna tıklama
users_single_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="users-single"]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", users_single_button)
users_single_button.click()
time.sleep(2)  

# 3. post butonuna tıklama
post_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="post"]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", post_button)
post_button.click()
time.sleep(2) 

# 4. register-successful butonuna tıklama
register_successful_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="register-successful"]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", register_successful_button)
register_successful_button.click()
time.sleep(2)  

# 5. login-successful butonuna tıklama
login_successful_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[data-id="login-successful"]'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", login_successful_button)
login_successful_button.click()
time.sleep(2)  

driver.quit()
