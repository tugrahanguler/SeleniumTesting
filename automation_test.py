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

# 1. Swagger butonuna tıklama
logo = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/api-docs"]'))
)
logo.click()

# Sayfanın yüklenmesi için zaman veriyoruz.
time.sleep(3)

# 2. POST butonuna tıklama
post_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='POST']"))
)
post_button.click()

# 3. "Try it out" butonuna tıklama
try_it_out_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.try-out__btn'))
)
try_it_out_button.click()

# username alanına değer girme
username_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.body-param__text'))
)
username_field.send_keys("tugraboramehmetali")

# email alanına değer girme
email_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.body-param__text'))
)
email_field.send_keys("yazılımkalite@example.com")

# password alanına değer girme
password_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea.body-param__text'))
)
password_field.send_keys("guvencetemelleri")

# 5. "Execute" butonuna tıklama
execute_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.execute'))
)
execute_button.click()

# 5 saniye sonrasında kapatıyoruz.
time.sleep(5)
driver.quit()
