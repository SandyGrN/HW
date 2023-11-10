'''
Вивеcти з API(приват та моно) курс валют для:
USA
EURO
GBR
PLN
Свою валюту
'''

import requests
res_monobank = requests.get('https://api.monobank.ua/bank/currency')
res_monobank.status_code
# for obj in res_monobank.json():
# print(f'Object is {obj}, \nType is{type(obj)}', end='\n\n')

my_currencies = {
    980: '🇺🇦',
    840: '🇺🇸',
    978: "🇪🇺",
    826: '🇬🇧',
    985: '🇵🇱',
    981: '🇬🇪'
}


my_rates = []
for obj in res_monobank.json():
    if obj['currencyCodeA'] in my_currencies and obj not in my_rates:
        my_rates.append(obj)


for obj in my_rates:
    if obj['rateCross'] != 0:
        print(f"Країна: {my_currencies[obj['currencyCodeA']]} Курс: {obj['rateCross']}")
    else:
        print(f"Країна: {my_currencies[obj['currencyCodeA']]} Купівля: {obj['rateBuy']} Продаж: {obj['rateSell']}")

# приват
res_privatbank = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
res_privatbank.status_code
res_privatbank.json()

new_currencies = {
    'USD': '🇺🇸',
    'EUR': '🇪🇺',
}

for item in res_privatbank.json():
    print(f"Країна: {new_currencies[item['ccy']]} Купівля {item['buy']} Продаж: {item['sale']}")


'''
- Написати Test  
- Вивеcти курс валюти від користувача
- Робити перевірки на status code
- Написати це в функцію
- Залити на git(flake8 use, requirments, config.cfg)
'''


def exchange_rate() -> str:
    url = 'https://api.monobank.ua/bank/currency'
    txt = 'Доступні для перевірки: \nдолар \nєвро \nзлотий \nларі \nфунт стерлінгів \nєна \nюань \nдирхам'
    user_input = input(f'{txt} \nВведіть назву валюти: ').casefold()
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()

        match user_input:
            case 'долар':
                return (f"Валюта: Долар Купівля: {r.json()[0]['rateBuy']} Продаж: {r.json()[0]['rateSell']}")
            case 'євро':
                return (f"Валюта: Євро Купівля: {r.json()[1]['rateBuy']} Продаж: {r.json()[1]['rateSell']}")
            case 'фунт стерлінгів':
                gpb = [i for i, d in enumerate(r.json()) if 826 in d.values()]
                return (f"Валюта: Фунт Стерлінгів Курс: {r.json()[int(gpb[0])]['rateCross']}")
            case 'ларі':
                gel = [i for i, d in enumerate(r.json()) if 981 in d.values()]
                return (f"Валюта: Ларі  Курс: {r.json()[int(gel[0])]['rateCross']}")
            case 'злотий':
                pln = [i for i, d in enumerate(r.json()) if 985 in d.values()]
                return (f"Валюта: Злотий Курс: {r.json()[int(pln[0])]['rateCross']}")
            case 'єна':
                jpy = [i for i, d in enumerate(r.json()) if 392 in d.values()]
                return (f"Валюта: Єна Курс: {r.json()[int(jpy[0])]['rateCross']}")
            case 'юань':
                cny = [i for i, d in enumerate(r.json()) if 156 in d.values()]
                return (f"Валюта: Юань Курс: {r.json()[int(cny[0])]['rateCross']}")
            case 'дирхам':
                aed = [i for i, d in enumerate(r.json()) if 784 in d.values()]
                return (f"Валюта: Дирхам Курс: {r.json()[int(aed[0])]['rateCross']}")
            case _:
                return ('На жаль, дані відсутні 😔 ')
    except requests.exceptions.RequestException as err:
        return ("OOps: Something Else", err)
    except requests.exceptions.HTTPError as errh:
        return ("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        return ("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        return ("Timeout Error:", errt)


print(exchange_rate())

# Practice
# 1. Create a program that will ask user to search a word.
# Search this word in Giphy (use their API).
# Return links to these GIFs as a result

from urllib import parse, request
import json

user_word = input('Введіть пошуковий запит: ')
url = "http://api.giphy.com/v1/gifs/search"

params = parse.urlencode({
  "q": user_word,
  "api_key": "tF42CAOHLF05sp2hrJJ6Z0oUyxOpfPIo",
  "limit": "1"
})

with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())

result = []
for i in data['data']:
    result.append(i['url'])


print(''.join(result))

# 2. Взяти API-weather, розпарсити і вивеcти погоду від користувача
# (вводить локацію, по цій локації повернеться погода, вологість і тд)
# https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа


api_key = '2209aeb64453cadeddb3f06b4296535a'
limit = 1
q = input('Введіть назву міста: ')
geocoding = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={q}&limit={limit}&appid={api_key}')

for i in geocoding.json():
    lat =i['lat']
    lon = i['lon']

res_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
weather = res_weather.json()['weather'][0]['main']
temp = round(res_weather.json()['main']['temp'] - 273.15, 2)
feels_like = round(res_weather.json()['main']['feels_like'] - 273.15, 2)
humidity = res_weather.json()['main']['humidity']
print(f'{q}: \nWeather🌤️: {weather} \n Temperature🌡️: {temp} °С \n Feels like 🌓: {feels_like} °С \n Humidity💧: {humidity} %')


# 3. Вивеcти всіх космонавтів(кількість і імена)
#  http://api.open-notify.org/astros.json

spaceman = requests.get('http://api.open-notify.org/astros.json')

names = []
for i in spaceman.json()['people']:
    names.append(i['name'])
print(f'Космонавти:', ' \n'.join(names), '\nКількість: ', spaceman.json()['number'])
