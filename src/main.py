import requests
# import json
#
# API_KEY = '1742416b16aa5203889d53b9e7b180b3'
#
# response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=Krasnodar&appid={API_KEY}")
#
# lat = response.json()[0]['lat']
# lon = response.json()[0]['lon']
# units = 'metric'
# lang = 'ru'
#
# response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang={lang}&appid={API_KEY}&units={units}")
#
# print(json.dumps(response.json(), indent=4, ensure_ascii=False))
try:
    response = requests.get('http://example.com')
    response.raise_for_status()
    raise requests.exceptions.HTTPError
except requests.exceptions.HTTPError:
    print("HTTP Error. Please check the URL.")
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

