import json
import requests


API_KEY = "cf79122146227cca6cfb2b437c5db51a"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        return weather_description, temperature
    else:
        print("Error: Could not retrieve weather data.")
        print("Response Code:", response.status_code)
        print("Response Body:", response.text)
        return None, None

def main():
    city = input("Enter the name of the city: ")
    weather_description, temperature = get_weather(city)

    if weather_description and temperature is not None:
        print(f"The weather in {city} is: {weather_description}.")
        print(f"The temperature is: {temperature} °C.")

if __name__ == "__main__":
    main()
