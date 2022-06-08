# Simulate 4 Dog Calendar

## Table of contents
* [Information](#information)
* [Software and applications](#software-and-applications)
* [Hardware](#hardware)
* [User guide](#user-guide)
* [For developers](#for-developers)

## Information
This project was made as a final project for the Karel de Grote Hogeschool during the course Internet of Things (IoT). The goal of the project is to make an app to plan dog walks while also looking at the weather at the time of the walk. what also needs to be included in this project is a way to check how many kilometers the dog has walked.

## Software and applications
* Pycharm  - > Development environment for python
* Arduino IDE - > Software to program arduino devices & hardware
* Kivy - > Frameork to build applications in python
* Firebase - > Database 
* Google calendar API
* Openweather API

## Hardware
* I2C 16x2 Arduino LCD Display module
* Arduino Nano 33 IoT
* Batterij 3.7 V - 2000 mAh
* MPU-6050 accelerometer 

## User guide
In this section i will go over how a user can interact with this app.
When starting up the app you will be allowed to do a couple of things:
1) Login with your google account to connect to the google calendar API
2) Change some settings & send user feedback
3) Continue to the core app features

![image](https://user-images.githubusercontent.com/72076173/172568077-dd3a002d-6c79-4a64-97a0-f76a8a00a9f6.png)

Next up you will reach a screen where you will decide what to do.
 1) "Plan your own walk". With this feature you can plan a walk at a specific time, you can select that time and insert the planning to your google calendar.

![image](https://user-images.githubusercontent.com/72076173/172569596-fe279818-63c3-44eb-97af-93f9a31faafa.png)
![image](https://user-images.githubusercontent.com/72076173/172569470-d44bc484-a888-429f-a726-5d6e89894c43.png)


 3) "let the app decide". The experimental feature: you can set how many walks you want to do this day & the amount of kilometers for each walk. the app will send the kilometers to the extra dog walk accessory & will plan in a few walks in your calendar

![image](https://user-images.githubusercontent.com/72076173/172571145-9f5eee8b-a031-4553-b01d-45576c3cbea0.png)

After that you will get a confirmation screen that will tell you that your calendar is updated succesfully.

![image](https://user-images.githubusercontent.com/72076173/163708201-b635c392-52c5-449f-8937-46263643e6a1.png)
![image](https://user-images.githubusercontent.com/72076173/163708228-4b39bc3d-f008-4ccf-9593-732ac78a21df.png)



