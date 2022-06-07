#!/usr/bin/env python
"""
Information about the script goes here
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
import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
#              VARIABLES              #
SCOPES = ['https://www.googleapis.com/auth/calendar']
#SCOPES = ['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar.events', 'https://www.googleapis.com/auth/calendar.events.readonly']
#              MAIN CODE              #


def logout():
    try:
        os.remove('Calendar/token.json')
    except Exception:
        pass


def refresh():
    creds = None
    if os.path.exists('Calendar/token.json'):
        creds = Credentials.from_authorized_user_file('Calendar/token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            os.remove('Calendar/token.json')
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('Calendar/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('Calendar/token.json', 'w') as token:
            token.write(creds.to_json())
    else:
        creds.refresh(Request())
    return creds


if __name__ == '__main__':  # run tests if called from command-line
    refresh()

