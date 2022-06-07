#!/usr/bin/env python
"""
Connection to the database
- Firebase: https://firebase.google.com/
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
import firebase_admin
from firebase_admin import credentials, db
from configurations import dbconfig, dbcredentials


#              MAIN CODE              #
def insertkilometers(kmInsert):
    try:
        cd = credentials.Certificate(dbcredentials())
        firebase_admin.initialize_app(cd, {"databaseURL": dbconfig()})
    except Exception:
        pass

    ref = db.reference("/")
    km = ref.get()
    for key, value in km.items():
        a = kmInsert
        ref.child(key).update({"km": a})
