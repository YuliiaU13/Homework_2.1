'''
Є вiдкритий API NASA який дозволяє за певними параметрами отримати данi у виглядi JSON
про фото зробленi ровером “Curiosity” на Марсi. Серед цих даних є посилання на фото
якi потрiбно розпарсити i потiм за допомогою додаткових запитiв скачати i зберiгти цi фото
як локальнi файли mars_photo1.jpg , mars_photo2.jpg . Завдання потрiбно зробити
використовуючи модуль requests
'''

import requests
from pathlib import Path

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


class ApiLoadMarsPhotos:
    def __init__(self, api_key, sol, camera, save_dir='mars_photos'):
        self.api_key = api_key
        self.sol = sol
        self.camera = camera
        self.save_dir = Path(save_dir)
        self.base_url = url
        self.save_dir.mkdir(parents=True, exist_ok=True)

    def select_photos(self):
        params = {
            'sol': self.sol,
            'camera': self.camera,
            'api_key': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

    def download_photos(self):
        data = self.select_photos()
        photo_count = 1

        for photo in data['photos']:
            img_url = photo['img_src']
            img_response = requests.get(img_url)
            img_response.raise_for_status()

            file_name = self.save_dir / f'mars_photo{photo_count}.jpg'
            with open(file_name, 'wb') as file:
                file.write(img_response.content)

            print(f'Downloaded: {file_name}')
            photo_count += 1


if __name__ == "__main__":
    downloader = ApiLoadMarsPhotos(api_key='DEMO_KEY', sol=1000, camera='fhaz')
    downloader.download_photos()
