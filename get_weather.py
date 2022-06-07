#!/usr/bin/env python
"""
Get current weather from API
- API documentation: https://openweathermap.org/api
- Convert Unix to datetime: https://devenum.com/unix-timestamp-to-datetime-in-python/ - DevEnum Team
"""
#          AUTHOR INFORMATION         #

#        _____
#      .'     `.
#     /  .-=-.  \   \ __
#     | (  C\ \  \_.'')
#     _\  `--' |,'   _/
#    /__`.____.'__.-' The coding snail~

__author__ = "Kevin Vervloet"
__email__ = "kevin.vervloet@student.kdg.be"
__Version__ = "(Code version)"
__status__ = "Development"
"""
TODO
- optimise code (remove test prints)
"""
#               IMPORTS               #
import requests
from geopy.geocoders import Nominatim
from configurations import weatherAPI
import datetime
import get_calendar
import random


#              MAIN CODE              #
def getweatherrandomly(wandelingen):  # function for option 2
    # Get longitude & langitude from location

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Antwerp")
    latitude = str(getLoc.latitude)
    longitude = str(getLoc.longitude)

    # API
    API_key = weatherAPI()
    base_url = "http://api.openweathermap.org/data/2.5/onecall?"
    Final_url = base_url + "lat=" + latitude + "&lon=" + longitude + "&appid=" + API_key + "&exclude=current," \
                                                                                           "minutely,daily," \
                                                                                           "alert" + "&units=metric "
    weather_data = requests.get(Final_url).json()
    lst = []
    lst2 = []
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    for data in weather_data["hourly"]:
        unix = data["dt"]  # get unix time from the json
        datetime_obj = datetime.datetime.utcfromtimestamp(int(unix))  # convert unix to a datetime
        times_from_api = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
        time_now = str(datetime.datetime.now())  # get current time
        weather = data["weather"][0]["main"]  # filter on weather type in json

        if time_now <= times_from_api:  # don't include times that happend in the past
            if times_from_api <= str(tomorrow):
                # print(weather + " " + times_from_api)
                lst.append(weather)
                lst2.append(times_from_api)

    length_time_list = len(lst2)                     # get the lenght of the list
    for random_number in random.sample(range(1, int(length_time_list)), int(wandelingen)):

        select_weather = lst[random_number]  # select a random time
        plannedhour = lst2[random_number]
        if select_weather == "Rain":
            text = f'Weather for {plannedhour} - {select_weather}. Be sure to bring a raincoat!'
            get_calendar.getcalendar(plannedhour, text)
            break
        print(select_weather, plannedhour)
        plannedhour = plannedhour[11:29]
        text = f'Weather for {plannedhour} - {select_weather}. Perfect time for a walk with your dog - Sent from Dog ' \
               f'Calendar App! '
        get_calendar.getcalendar(plannedhour, text)
        # send to calendar ... ->


def weatherhourly(plannedhour):  # function for option 2

    hour_format = "%H:%M:%S"  # format datetime in hour/min/sec
    dt_hour = datetime.datetime.strptime(plannedhour, hour_format)
    a = (dt_hour.replace(second=0, microsecond=0,
                         minute=0, hour=dt_hour.hour) + datetime.timedelta(
        hours=dt_hour.minute // 30))  # round the time
    walk = a.strftime('%H:%M:%S')  # remove day, year & month

    # Get longitude & langitude from location

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Antwerp")
    latitude = str(getLoc.latitude)
    longitude = str(getLoc.longitude)
    # city_name = "Antwerp"

    # API
    API_key = weatherAPI()
    base_url = "http://api.openweathermap.org/data/2.5/onecall?"
    Final_url = base_url + "lat=" + latitude + "&lon=" + longitude + "&appid=" + API_key + "&exclude=current," \
                                                                                           "minutely,daily," \
                                                                                           "alert" + "&units=metric "

    weather_data = requests.get(Final_url).json()

    for data in weather_data["hourly"]:
        unix = data["dt"]  # get unix time from the json
        datetime_obj = datetime.datetime.utcfromtimestamp(int(unix))  # convert unix to a datetime
        times_from_api = datetime_obj.strftime("%H:%M:%S")
        weather = data["weather"][0]["main"]  # filter on weather type in json

        if times_from_api == str(walk):
            if weather == "Rain":  # check for rain
                text = f'Weather for {plannedhour} - {weather}. Be sure to bring a raincoat!'
                get_calendar.getcalendar(plannedhour, text)
                break
            else:
                text = f'Weather for {plannedhour} - {weather}. Perfect time for a walk with your doggie!'
                get_calendar.getcalendar(plannedhour, text)
                break


# if __name__ == '__main__':  # run tests if called from command-line
#    getweatherrandomly()
