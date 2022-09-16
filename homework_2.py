import requests
import os
import json

# Определяем класс
class YaUploader:

    def __init__(self): # Определяем переменные функции
        self.url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload' # URL на заливку файла
        self.token = 'y0_AgAAAABkk8QRAADLWwAAAADO3RBMg-EGtKtrQyu0lhQ8Ueo2wUeaEG4' # Сюда токен пользователя (сейчас стоит твой)
        self.headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'} # Параметры запроса на авторизацию

    def upload(self, file_path:str): # Определяем переменные загрузки файла
        params = {'path': os.path.basename(file_path), 'overwrite': True} # Указываем путь с именем до БУДУЩЕГО файла на Я.диске, ставим перезапись по-умолчанию
        res = requests.get(self.url, headers=self.headers, params = params) # Запрашиваем у API ulr-адрес для заливки файла. Генерится уникальный для каждого файла
        link = res.json()['href'] # Выгружаем url из запрошенного ответа
        requests.put(link, files={'file': file_path}) # Заливаем файл

if __name__ == '__main__':
    file_path = 'C:\\Users\\ShariQue\\Downloads\\KEK.jpeg'
    YaUploader().upload(file_path)

