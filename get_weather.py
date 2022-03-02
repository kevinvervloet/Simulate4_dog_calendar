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

#               IMPORTS               #
import requests
from geopy.geocoders import Nominatim
from pprint import pprint
from configurations import weatherAPI
from datetime import datetime


#              MAIN CODE              #
def getweather():
    # Get longitude & langitude from location

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Antwerp")
    latitude = str(getLoc.latitude)
    longitude = str(getLoc.longitude)
    city_name = "Antwerp"

    # API
    API_key = weatherAPI()
    base_url = "http://api.openweathermap.org/data/2.5/onecall?"
    Final_url = base_url + "lat=" + latitude + "&lon=" + longitude + "&appid=" + API_key + "&exclude=current," \
                                                                                           "minutely,daily," \
                                                                                           "alert" + "&units=metric "
    weather_data = requests.get(Final_url).json()
    print("\nHourly data for " + city_name + ":\n")

    for data in weather_data["hourly"]:
        unix = data["dt"]                                      # get unix time from the json
        datetime_obj = datetime.utcfromtimestamp(int(unix))    # convert unix to a datetime
        time_now = str(datetime.now())[11:19]                  # get current time
        weather = data["weather"][0]["main"]                   # filter on weather type in json

        if data["weather"][0]["main"] == "Rain":               # check for rain
            pass

        if datetime_obj.strftime("%H:%M:%S") <= str(time_now):
            pass
        else:

            print(datetime_obj.strftime("%H:%M:%S"), weather)


if __name__ == '__main__':  # run tests if called from command-line
    getweather()
