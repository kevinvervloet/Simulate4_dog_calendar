#!/usr/bin/env python
"""
Insert the correct km in the database
"""

#               IMPORTS               #
import firebase_admin
from firebase_admin import credentials, firestore, db
import json
from configurations import dbconfig
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
def getkm(kmInsert):
    cd = credentials.Certificate("F")
    firebase_admin.initialize_app(cd, {"databaseURL": ""})

    ref = db.reference("/")
    km = ref.get()
    for key, value in km.items():
        a = kmInsert
        ref.child(key).update({"km": a})


#if __name__ == '__main__':  # run tests if called from command-line
    #getkm()
