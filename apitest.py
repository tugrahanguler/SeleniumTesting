import requests

API_KEY = "reqres-free-v1" # Örnek sitemizden aldığımız api keyi tanımlıyoruz.

# Kullanıcıları listeleme testi.
def test_get_users():
    url = "https://reqres.in/api/users"
    headers = {
        "x-api-key": API_KEY 
    }
    response = requests.get(url, headers=headers)
    
    # Başarılı durum kontrolü için senaryo.
    assert response.status_code == 200
    assert "data" in response.json()  
    assert len(response.json()["data"]) > 0 # En az bir user olduğunu kontrol ediyoruz.

# Kullanıcı oluşturma testi.
def test_create_user():
    url = "https://reqres.in/api/users"
    data = {
        "name": "John Doe",
        "job": "Software Engineer"
    }
    headers = {
        "x-api-key": API_KEY  
    }
    response = requests.post(url, json=data, headers=headers)
    
    assert response.status_code == 201 
    assert "name" in response.json()  
    assert response.json()["name"] == "John Doe"  

# Kullanıcı güncelleme testi
def test_update_user():
    url = "https://reqres.in/api/users/2"  # ID'si 2 olan kullanıcının üzerinde güncelleme uygulamayı deniyoruz.
    data = {
        "name": "Jane Doe",
        "job": "Project Manager"
    }
    headers = {
        "x-api-key": API_KEY 
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200  
    assert response.json()["name"] == "Jane Doe"  
    assert response.json()["job"] == "Project Manager"

# Kullanıcı silme testi
def test_delete_user():
    url = "https://reqres.in/api/users/2"  # ID'si 2 olan kullanıcıyı silme testi yapıyoruz.
    headers = {
        "x-api-key": API_KEY  
    }
    response = requests.delete(url, headers=headers)
    
    assert response.status_code == 204  # 204 no content kodunu test ediyoruz.

# Varolmayan bir endpoint testi tepkisi.
def test_invalid_endpoint():
    url = "https://reqres.in/api/unknown/23"  # Geçersiz bir endpoint belirliyoruz bu şekilde bir endpoint bulunmuyor. Bu durumda bize 404 not found hatası döndürmeli.
    headers = {
        "x-api-key": API_KEY  
    }
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 404  
    assert response.json() == {} # Boş veri döndürülmesi gerek.

# Eksik veri girişi testi.
def test_invalid_create_user():
    url = "https://reqres.in/api/users"
    data = {
        "name": ""  # Job keyi tanımlanmıyor ve name'yi boş bırakıyoruz.
    }
    headers = {
        "x-api-key": API_KEY 
    }
    response = requests.post(url, json=data, headers=headers)
    
    assert response.status_code == 400

# Performans testi
def test_api_performance():
    url = "https://reqres.in/api/users"
    headers = {
        "x-api-key": API_KEY  
    }
    response = requests.get(url, headers=headers)
    
    assert response.elapsed.total_seconds() < 1  # Yanıt süresi 1 saniyeden az olmalı.

