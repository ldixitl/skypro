import json
import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv

# import datetime
#
# date_string = "08-03-2022 15:45:00"
# date_obj = datetime.datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
# print(date_obj)
# print(type(date_obj))

# def get_currency_rate(currency):
#     url = "https://www.cbr-xml-daily.ru/daily_json.js"
#
#     response = requests.get(url)
#     result = {
#         "Currency code": currency,
#         "Rate": response.json()["Valute"][currency]["Value"]
#     }
#
#     return json.dumps(result, indent=4)
#
# print(get_currency_rate("EUR"))

# def get_github_users(users_list):
#     results = []
#     for user in users_list:
#         user_info = get_user_info(user)
#         user_repos = get_user_repos(user)
#
#         result = {
#             "Login": user_info["login"],
#             "Count repos": user_info["public_repos"],
#             "Repos": user_repos
#         }
#         results.append(result)
#
#     return json.dumps(results, indent=4)
#
#
# def get_user_info(user):
#     url = f"https://api.github.com/users/{user}"
#     response = requests.get(url)
#
#     return response.json()
#
#
# def get_user_repos(user):
#     url = f"https://api.github.com/users/{user}/repos"
#     response = requests.get(url)
#     repos = []
#     for repo in response.json():
#         repos.append(repo["name"])
#
#     return repos
#
#
# print(get_github_users(["ldixitl", "test"]))

# load_dotenv(".env")
# API_KEY_WEATHER = os.getenv("API_KEY_WEATHER")
#
# url = "https://api.openweathermap.org/data/2.5/weather"
#
#
# def get_coords(city: str) -> tuple:
#     # Получение координат города
#     response = requests.get(
#         f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY_WEATHER}"
#     )
#
#     lat = response.json()[0]["lat"]
#     lon = response.json()[0]["lon"]
#
#     return lat, lon
#
#
# def get_weather(lat: float, lon: float) -> float:
#     payload = {
#         "lat": lat,
#         "lon": lon,
#         "units": "metric",
#         "lang": "ru",
#         "appid": API_KEY_WEATHER,
#     }
#
#     response = requests.get(url, params=payload)
#
#     return response.json()["main"]["temp"]
#     # print(json.dumps(response.json(), indent=4, ensure_ascii=False))
#
#
# @patch("requests.get")
# def test_get_weather(mock_get):
#     mock_get.return_value.json().return_value = {"main": {"temp": 3.32}}
#     assert get_weather(1, 1)
#     mock_get.assert_called_once_with(
#         f"https://api.openweathermap.org/data/2.5/weather",
#         params={
#             "lat": 1,
#             "lon": 1,
#             "units": "metric",
#             "lang": "ru",
#             "appid": API_KEY_WEATHER,
#         },
#     )
#
#
# if __name__ == "__main__":
#     lat, lon = get_coords("Krasnodar")
#     print(get_weather(lat, lon))

# url = "https://api.apilayer.com/exchangerates_data/convert"
#
# payload = {
#   "amount": "1200",
#   "from": "USD",
#   "to": "RUB"
# }
# headers= {
#   "apikey": "rcOTu2LUMiwfaP03DnnrnROCjUL1yqRz"
# }
#
# response = requests.get(url, headers=headers, params=payload)
#
# status_code = response.status_code
# result = response.text
#
# print(result)
# print(status_code)
