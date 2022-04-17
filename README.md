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


## Hardware
* I2C 16x2 Arduino LCD Display module
* Arduino Nano 33 IoT
* Batterij 3.7 V - 2000 mAh
* MPU-6050 accelerometer 

## User guide
![image](https://user-images.githubusercontent.com/72076173/163707994-f7b18d0b-6829-4044-b6d0-820f82544c4b.png)

Users that want to use the dog calendar app will be able to use two main features. After you click passed the home screen, you will see two buttons:
 1) "Plan your own walk". The main feature is to plan in a dog walk from the app, the app will check the weather for that time. you will get a notification when it's almost time for your dog walk. This is very helpful if you have multiple people in your household and they need to be aware to take their dog out from time to time.

![image](https://user-images.githubusercontent.com/72076173/163708148-8845d828-d72e-4631-a3d9-8f206d94b724.png)

 2) "let the app decide". The experimental feature: you can set how many walks you want to do this day & the amount of kilometers for each walk. the app will send the kilometers to the extra dog walk accessory & will plan in a few walks in your calendar

![image](https://user-images.githubusercontent.com/72076173/163708019-75f0c1c8-fc6c-4ef2-b859-4d632397a4e4.png)

After you used one if these features the app will give you a confirmation message when you succesfully inserted a new event in your calendar.

![image](https://user-images.githubusercontent.com/72076173/163708201-b635c392-52c5-449f-8937-46263643e6a1.png)
![image](https://user-images.githubusercontent.com/72076173/163708228-4b39bc3d-f008-4ccf-9593-732ac78a21df.png)


## For developers

