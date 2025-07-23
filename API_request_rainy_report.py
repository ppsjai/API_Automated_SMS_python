# apilist.fun to explore more API like this
# to see detailed weather ventusky.com
import requests
# twilio API service is used for send msg,phone using any country code create an account in twilio API in order to performe this code
from twilio.rest import Client

open_weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "your_API_key_from_twilio"                           #copy your api token from your id
account_sid = "your_account_sid_from_twilio"                   #copy your account sid from your id
auth_token = "your_authendication_key_from_twilio"             #copy your token from your id [AuthToken]

# in order to perform in google ventusky.com check where was really raining in that world map
# and get that longititude and latitude paste it in lat and lon
# sample latitude and longitude from india,kerela
# "lat": 8.877414834156072,
# "lon": 76.58544513522764,
weather_params = {
    "lat": your latitude,
    "lon": your longitude,
    "appid": api_key,
    "cnt": 3,
}

response = requests.get(open_weather_endpoint, params=weather_params)
response.raise_for_status()
weather_info = response.json()

might_be_rain_today = False # the loop will stop it will execute single time
for hour_info in weather_info["list"]:
    condition_info = hour_info["weather"][0]["id"]  # gives id info if use print key
    if int(condition_info) < 700: # it will result you as raining
        might_be_rain_today = True
if might_be_rain_today:
    client = Client(account_sid, auth_token)
    message = client.messages.\
        create(
        body="It might be any weather in your give location write the text in here",
        from_="paste the random generated number from tiwilio", # in order to paste it you must create an random generate number from tiwilio
        to="+91your number from tiwilio",
    )
    print(message.status)
# copy your dictionary format output and paste it in json viewer website go for text and paste over there
# now if we check in jason viewer website see viewer option click all the + box there we can find as it was raining or not
