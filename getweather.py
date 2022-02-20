#!/usr/bin/env python
"""
Get current weather from API
"""

#               IMPORTS               #
import requests
from geopy.geocoders import Nominatim
from pprint import pprint

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


#              VARIABLES              #

#              MAIN CODE              #
def getweather():
    # Get longitude & langitude from location

    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("deurne")
    latitude = getLoc.latitude
    longitude = getLoc.longitude

    # Get forcast
    API_key = ""

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Antwerpen"
    Final_url = base_url + "appid=" + API_key + "&q=" + city_name

    weather_data = requests.get(Final_url).json()

    print("\nCurrent Weather Data Of " + city_name + ":\n")
    pprint(weather_data)

    a = weather_data["weather"][0]["main"]

#    if a == "Rain":
#        print("it's going to rain, take an umbrella")
#    else:
#        pprint(a)


if __name__ == '__main__':  # run tests if called from command-line
    getweather()
