#!/usr/bin/env python
"""
configurations file. In this file all the project secrets will be stored
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


#              MAIN CODE              #
def pwd():
    pwd_email = "kdgiot33!"
    return pwd_email


def dbconfig():
    databaseURL = "https://pet-friend-29364-default-rtdb.europe-west1.firebasedatabase.app/"
    return databaseURL


def dbcredentials():
    dbcred = "Firebase/pet-friend-29364-firebase-adminsdk-c272t-7304f5b190.json"
    return dbcred


def weatherAPI():
    API_KEY = "5bb76bcc0cada30df4bfc4e768a6ec49"
    return API_KEY
