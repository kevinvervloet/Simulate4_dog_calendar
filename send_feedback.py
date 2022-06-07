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

import smtplib
import configurations
import uuid
#              MAIN CODE              #


def send_mail(feedback):
    Sender_email = "portfolio2iot@gmail.com"
    rec_email = "portfolio2iot@gmail.com"
    unique_id = uuid.uuid4()
    pwd = configurations.pwd()
    message = 'Subject: {}\n\n{}'.format(f"User feedback No. {unique_id}", feedback)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(Sender_email,pwd)
        server.sendmail(Sender_email,rec_email,message)

    except Exception:
        print("something went wrong")

