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
from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


#              VARIABLES              #
CLIENT_SECRET_FILE = 'Calendar/Client_Secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']
calendar_id = 'eumodh7n14f2ticajh23lrbtpo@group.calendar.google.com'


#              MAIN CODE              #
def main():
  pass


if __name__ == '__main__':
    main()