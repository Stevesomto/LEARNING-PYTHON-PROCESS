# WHAT IS AN API. APPLICATION PROGRAMMING INTERFACE IS A SET OF RULES AND TOOLS THAT ALLOW DIFFERENT SOFTWARE TO COMMUNICATE WITH EACH OTHER. IT ENABLES DEVELOPERS TO FETCH DATA, SEND DATA AND INTERACT WITH EXTERNAL SERVICES

# REQUEST -  A CALL TO API. USE TO FETCH DATA
# RESPONSE - DATA RETURNED BY API
# END POINT - SPECIFIC URL THAT PROVIDES ACCESS TO AN API FUNCTION
# API KEY - A UNIQUE IDENTIFIER FOR ACCESSING API SECURELY

# EXAPLES OF API END POINTS
# https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY

# https://api.stephenweathermap.com/data/2.2/weather?q=Owerri&appid=33KGJSOT0093NFHTT

# pip install requests
import requests 
API_KEY = "681202c782e4a6d04935a962ea060cfb"  # MY UNIQUE API KEY FOR OPEN WEATHER MAP
city = input("Enter the name of the city you want to check: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

# TO FETCH WEATHER DATA
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    print(f"Here is the details of {city}:\n", weather_data)
else:
    print(f"Error: {response.status_code}")
