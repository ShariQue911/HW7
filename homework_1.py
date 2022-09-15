import pandas as pd
import requests

# Основные URL
url_base = 'https://akabab.github.io/superhero-api/api'
url_cached = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'

# Руты URL
url_all = '/all.json'

# Выгрузка информации о всех суперах в json
result = requests.get(url_cached+url_all)
if result.status_code != 200: # Error-check невыполненного реквеста
    print(result.status_code)
    exit()
data = result.json()

# Работа с датафреймом

df_data = pd.json_normalize(data) # Перевод выгрузки в датафрейм
supers_list = ['Hulk', 'Captain America', 'Thanos'] # Список суперов для поиска
df_data_temp = df_data[df_data['name'].isin(supers_list)] # Фильтр временной таблицы по списку суперов для поиска
df_result = df_data_temp[df_data_temp['powerstats.intelligence'] == df_data_temp['powerstats.intelligence'].max()][['name','powerstats.intelligence']] # Вывод имени самого умного (или умных) суперов из списка
print(df_result)