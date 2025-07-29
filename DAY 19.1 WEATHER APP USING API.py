# WEATHER APP USING OPEN WEATHER MAP API
import requests

# API SET UP
API_KEY = "681202c782e4a6d04935a962ea060cfb"  # MY UNIQUE API KEY FOR OPEN WEATHER MAP
BASE_URL = f"https://api.openweathermap.org/data/2.5/weather"

# GET WEATHER DATA
def get_weather(city):
    try: 
        url = f"{BASE_URL}?q = {city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']}°C",
                "Weather": data["weather"][0]["description"].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']} m/s",
            }
            return weather
        elif response.status_code == 404:
            print("City not found")
        else:
            print(f"An error occured. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error ouccrend {e}")
    return None

# DISPLAY THE WEATHER INFORMATION 
def display_info(weather):
    print("\n---- Weather Information---")
    for key, value in weather.items():
        print(f"{key}: {value}")

# MAIN PROGRAM LOOP

while True:
    print("\n---- Weather App---")
    city = input("Enter a city name (or q to quit): ").strip()
    if city.lower() == "q":
        print("Thank you for your time!")
        break
    weather = get_weather(city)
    if weather:
        display_info(weather)
    
    