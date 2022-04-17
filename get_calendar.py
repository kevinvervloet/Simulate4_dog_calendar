#!/usr/bin/env python
"""
Introduction video on Google calendar API - https://www.youtube.com/watch?v=eRHvfNKcwMQ from Cndro
How to convert a string to datetime - https://pythonguides.com/convert-a-string-to-datetime-in-python/
"""

#               IMPORTS               #
import os
import sys

sys.path.insert(1, 'Calendar/')
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from refreshtoken import refresh

#              VARIABLES              #
CLIENT_SECRET_FILE = 'Calendar/Client_Secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
calendar_id = 'eumodh7n14f2ticajh23lrbtpo@group.calendar.google.com'


#              MAIN CODE              #
def getcalendar(plannedhour, text):
    now = datetime.now()
    daynow = now.strftime('%Y-%m-%d')

    # convert str to time
    formathour = "%H:%M:%S"
    dt_hour = datetime.strptime(plannedhour, formathour)  # convert user inputted str to datetime
    a = dt_hour + timedelta(minutes=30)  # Add 30 minutes to the inputted time
    add_half_hour = a.strftime('%H:%M:%S')  # remove year, month & day from the time

    # The event for your calendar
    eventdata = {
        "organizer": {
            "displayName": 'Dog Calendar App',
        },
        'creator': {
            "displayName": 'Dog Calendar App',
            "creator.self": True,
        },
        'summary': '🐕 Dog walk! 🐕',
        'description': text,
        'start': {
            'dateTime': daynow + 'T' + plannedhour,
            'timeZone': 'Europe/Brussels',
        },
        'end': {
            'dateTime': daynow + 'T' + add_half_hour,
            'timeZone': 'Europe/Brussels',
        },
        "anyoneCanAddSelf": True,
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    # Connect to the Google calendar API

    # Send Event to Google calendar
    service = build(API_NAME, API_VERSION, credentials=refresh())

    events = service.events().insert(calendarId=calendar_id, body=eventdata).execute()
    print('Event created: %s' % (events.get('htmlLink')))

# if __name__ == '__main__':
#   setcred()
