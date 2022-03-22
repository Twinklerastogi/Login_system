import requests


def api_data():
    api_key = "27e2d39f20294a90adce49455f4cc6e2"
    api_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = input("Enter city name : ")
    url = api_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    data = response.json()
    return data






