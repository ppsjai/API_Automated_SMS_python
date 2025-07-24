# create an account in pythonanywhere to perform this code
# TODO-1: After creating an account it will open you an dash board in that top you can see file option go to that and click upload
#          upload this code from your desktop once it done
# TODO-2: click that file once it open you see an CLI in that CLI we are going to create environment variable for these below 2 line of code 
# api_key = os.environ.get("OWM_API_KEY")
# auth_token = os.environ.get("AUTH_TOKEN")#
# TODO-3: In CLI use this commands export OWM_API_KEY=your api key form twilio and press enter use env cmd to check it has created envronment variable or not once you find it
# TODO-4: same as this commands export AUTH_TOKEN=your authentication key from twilio press enter and check using this env cmd it has created or not
# TODO-5: excute this commands python3 your_uploaded_file_name.py now it will send an sms to that number dont forget to save it. 
# TODO-6: open home page of pythonanywhere dashboard in a new tab
# TODO-7: go to tasks option create an task there we can see server time in UTC format by creating this task give extra time based on UTC time running right now
# TODO-8: then in commands--> export OWM_API_KEY=your API key; export AUTH_TOKEN=your aunthentication key; python3 your_uploaded_file_name.py use this script in commands option once it done click to save it
# TODO-9: refresh the page if the UTC time was exceded given tike re-edit the UTC time with extra 4 or 5 min right now in UTC time to check our code was running or not 
# TODO-10: once it running daily you get message on that time we have give in UTC time format but we can able to change it
# TODO-11: In google search for UTC with your country time cordination with that help of we can set the correck UTC time in our task section
# TODO-12: check what time is in your country based on that it will provide an UTC time use that UTC time only in order to execute this program
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

open_weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "your account sid from Twilio API"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": your longitude,#8.877414834156072,
    "lon": your latitude,#76.58544513522764,
    "appid": api_key,
    "cnt": 8,
}

response = requests.get(open_weather_endpoint, params=weather_params)
response.raise_for_status()
weather_info = response.json()

might_be_rain_today = False
for hour_info in weather_info["list"]:
    condition_info = hour_info["weather"][0]["id"]
    if int(condition_info) < 700:
        might_be_rain_today = True
if might_be_rain_today:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.\
        create(
        body="It's gonna rain right now go and grab the umbrella before you went outside | ~ |",
        from_="+1Auto generate should be here",
        to="+91your number",
    )
    print(message.status)
