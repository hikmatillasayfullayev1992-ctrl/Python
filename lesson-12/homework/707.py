import requests
url = "https://api.siat.stat.uz/media/uploads/sdmx/sdmx_data_225.json"
respond = requests.get(url)
data = respond.json()
for i in data[0]["metadata"]:
    print(i["name_uz"])

import os
asosiy_papka = "Aktyorlar"
asosiy_path = os.path.join(os.getcwd(), asosiy_papka)
os.makedirs(asosiy_path, exist_ok=True)
for i in range(1, 51):
    aktyor_papka = f"Aktyor_{i}"
    path = os.path.join(asosiy_path, aktyor_papka)
    os.makedirs(path, exist_ok=True)
print('Aktyorlar')
