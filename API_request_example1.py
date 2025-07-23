# for this first create an account in Twilio and set it for SMS there you can find your api_key copy and paste it in this code
# go to google and search lattitute and longitude to find out your location lattitute and longitude once it done
# copy lattitude and paste in lat in our dictionary same as longitude in lon
import requests

# this API will give you an every 3 hour of refresh data of current weather report
open_weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_API_key_from_Twilio_palform"

weather_params = {
    "lat": your_longititude in google,
    "lon": your longitude in google,
    "appid": api_key,
    "cnt": 3, 
} # "cnt": 3, it will give 3 set of dictionary info

response = requests.get(open_weather_endpoint, params=weather_params)
print(response.status_code) # to check API working or not
print(response.json())
# once we get data in JSON format check in json viewer website to to list section to see all details we have been listed over there
# now we have to create it might be rain today or not we can able to check it

# in JSON viewer click list and any other number click on weather and click on the number here we can find id
# my id was 804 now we have go and check in weather icon it show's me clouds=overcast clouds: 85-100% so it might be rain
# links:https://openweathermap.org/weather-data --> keywords
# https://openweathermap.org/weather-conditions --> code for what is the weather condition right now
