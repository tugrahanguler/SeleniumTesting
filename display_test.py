from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver için Service nesnesini oluşturup path belirliyoruz.
service = Service(executable_path="chromedriver/chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://reqres.in")

# 1. Header ogesinin dogru sekilde gorunup gorunmedigini kontrol ediyoruz.
header = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)
assert header.is_displayed(), "Header ogesi gorunur degil!"
print("Header ogesi basariyla gorunur ve yerlesmis.")

# 2. Buton ogesinin dogru sekilde gorunup gorunmedigini kontrol ediyoruz.
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/api-docs"]'))
)
assert button.is_displayed(), "Buton ogesi gorunur degil!"
print("Buton ogesi basariyla gorunur ve tiklanabilir.")

# 4. Sayfa ogesinin dogru konumda olup olmadigini kontrol ediyoruz. (footer)
footer = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.TAG_NAME, "footer"))
)
footer_position = footer.location
assert footer_position["y"] > 0, "Footer ogesi sayfada duzgun yerlestirilmemis"
print("Footer ogesi basariyla sayfada duzgun yerlestirilmis.")

# 5. Sayfa basligini kontrol ediyoruz.
page_title = driver.title
assert "Reqres - A hosted REST-API ready to respond to your AJAX requests" in page_title, "Sayfa basligi beklenen degeri tasimiyor!"
print(f"Sayfa basligi '{page_title}' basariyla goruntuleniyor.")

# 6. Resim ogesinin dogru sekilde gorunup gorunmedigini kontrol ediyoruz.
image = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "img"))
)
assert image.is_displayed(), "Resim ogesi gorunur degil!"
print("Resim ogesi basariyla gorunur.")

driver.quit()
