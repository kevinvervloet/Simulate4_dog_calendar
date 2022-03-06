#!/usr/bin/env python
"""
Introduction video on Google calendar API - https://www.youtube.com/watch?v=eRHvfNKcwMQ from Cndro
How to convert a string to datetime - https://pythonguides.com/convert-a-string-to-datetime-in-python/
"""
import os
import requests
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from requests.structures import CaseInsensitiveDict
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import json
from pprint import pprint
import time
#               IMPORTS               #


#              VARIABLES              #
CLIENT_SECRET_FILE = 'Calendar/Client_Secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
calendar_id = 'eumodh7n14f2ticajh23lrbtpo@group.calendar.google.com'
SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly',
          'https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar.events.readonly']


#              MAIN CODE              #
def main(plannedhour):
    now = datetime.now()
    daynow = now.strftime('%Y-%m-%d')

    # convert str to time
    format = "%H:%M:%S"
    dt_hour = datetime.strptime(plannedhour, format)  # convert user inputted str to datetime
    a = dt_hour + timedelta(minutes=30)               # Add 30 minutes to the inputted time
    add_half_hour = a.strftime('%H:%M:%S')            # remove year, month & day from the time

    eventdata = {
        'summary': 'Dog walk!',
        'description': 'You have a planned walk with your doggie!',
        'start': {
            'dateTime': daynow + 'T' + plannedhour,
            'timeZone': 'Europe/Brussels',
        },
        'end': {
            'dateTime': daynow +'T'+ add_half_hour,
            'timeZone': 'Europe/Brussels',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    # Connect to the Google calendar API
    creds = None
    if os.path.exists('Calendar/token.json'):
        creds = Credentials.from_authorized_user_file('Calendar/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('Calendar/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('Calendar/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build(API_NAME, API_VERSION, credentials=creds)

    events = service.events().insert(calendarId=calendar_id, body=eventdata).execute()
    print('Event created: %s' % (events.get('htmlLink')))
