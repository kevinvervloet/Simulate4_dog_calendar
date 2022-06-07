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
def dbconfig():
    databaseURL = "Database URL goes here"
    return databaseURL


def dbcredentials():
    dbcred = "Firebase credentials go here"
    return dbcred


def weatherAPI():
    API_KEY = "API KEY"
    return API_KEY
