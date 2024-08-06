'''
У venv Python встановiть Flask за допомогою команди pip install flask
Створiть у окремiй директорiї файл app.py та скопiюйте у нього код файлу app.py який приведено нижче в початкових даних.
Запустiть http сервер за допомогою команди python app.py
Сервер стартує за базовою адресою http://127.0.0.1:8080
Враховуючи документацiю яку наведено нижче вам потрiбно написати код який використовуючи модуль request
зробить через POST upload якогось зображення на сервер, за допомогою GET отримає посилання на цей файл и
потiм за допомогою DELETE зробить видалення файлу з сервера
'''

import requests
filename = 'mars_photo1.jpg'


print('Завантаження зображення:')
image_path = 'mars_photo1.jpg'

with open(image_path, 'rb') as image_file:
    upload_url = 'http://127.0.0.1:8080/upload'
    response = requests.post(upload_url, files={'image': image_file})

    if response.status_code == 201:
        data = response.json()
        image_url = data['image_url']
        print(f'Image uploaded! URL: {image_url}')
    else:
        print(f'Failed to upload image. Status code: {response.status_code}')


print('Отримання URL завантаженого зображення:')

get_image_url = f'http://127.0.0.1:8080/image/{filename}'

response = requests.get(get_image_url, headers={'Content-Type': 'text'})

if response.status_code == 200:
    data = response.json()
    image_url = data['image_url']
    print(f'Image URL: {image_url}')
else:
    print(f'Failed to get image URL. Status code: {response.status_code}')


print('Видалення зображення:')

delete_url = f'http://127.0.0.1:8080/delete/{filename}'
response = requests.delete(delete_url)

if response.status_code == 200:
    print(f'Image {filename} deleted successfully')
else:
    print(f'Failed to delete image. Status code: {response.status_code}')