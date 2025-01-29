import requests

def get_weather(city):
    api_key = "d9751904829956ac6d480f30fe44527d"
    base_url= "https://api.openweathermap.org/data/2.5/weather"
    params = {'q':city, 'appid':api_key,'units': 'metric'}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"city: {data['name']}")
        print(f"Temperature: {data['main']['temp']} C")
        print(f"weather:{data['weather'][0]['description']}")

    else:
        print("City not found")



def get_forecast(city):
    api_key = "d9751904829956ac6d480f30fe44527d"
    base_url = "https://pro.openweathermap.org/data/2.5/forecast"
    params = {'q':city, 'appid':api_key,'units': 'metric'}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print("Weather forecast for " + data['city']['name'])
        print(f"{data['cnt']}forecast retrive")

        for forecast in data['list'][:4]:
            Temperature = forecast['main']['temp']
            description = forecast ['weather'][0]['description']
            print(f"Temp: {Temperature},Decs: {description}")

    else:
        print("City not found")


city = input("Enter a City:")
get_weather(city)
get_forecast(city)
                   