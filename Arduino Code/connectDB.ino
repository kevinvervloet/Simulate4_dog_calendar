/* INFORMATION
 *  
 *   Documentation firebase library for arduino https://github.com/mobizt/Firebase-Arduino-WiFiNINA for ESP32 
 *  
 *  author = "Kevin Vervloet"
 *  email = "kevin.vervloet@student.kdg.be"
 *  status = "Development"
*/

#include "Firebase_Arduino_WiFiNINA.h"
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Arduino_LSM6DS3.h>

// configure wifi & firebase settings
#define DATABASE_URL " " //pet-friend-29364-default-rtdb.firebaseio.com or <databaseName>.<region>.firebasedatabase.app
#define DATABASE_SECRET " "
#define WIFI_SSID " "                    
#define WIFI_PASSWORD " "          

//Define Firebase data object
FirebaseData fbdo;
LiquidCrystal_I2C lcd(0x20,16,2);

// define the counter
int count = 0;



// Setup
void setup()
{
  Serial.begin(9600);
    
  delay(100);
  lcd.init();
  lcd.backlight();
  lcd.home();
  lcd.clear();
  int status = WL_IDLE_STATUS;
  while (status != WL_CONNECTED)
  {
    status = WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    delay(100);
  }
  Serial.println("Arduino device connected to WiFi");

  //Provide the autntication data
  Firebase.begin(DATABASE_URL, DATABASE_SECRET, WIFI_SSID, WIFI_PASSWORD);
  Firebase.reconnectWiFi(true);
  Serial.println("Firebas connection OK");
  lcd.println("Connected !");
  
  
  while (!Serial);

  if (!IMU.begin()) {
    lcd.clear();
    lcd.println("IMU Failed");
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  Serial.println("IMU SUCCESS");
  
  String path = "/km/km";

  if (Firebase.get(fbdo, path)) {
    Serial.println("Dog Calendar, current km value is: " + fbdo.stringData());
    //lcd.setCursor(0, 1);
    //lcd.print("km: " + fbdo.stringData());
  }
  else
  {
    Serial.println("error, " + fbdo.errorReason());
  }
   
}



void loop(){
  float calculaton = 0.000762;  // average meters for 1 step (human) https://reviews.tn/en/wiki/how-far-is-1-meter-in-steps/
  float x, y, z;
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    if (y > 1) {
    
    ++count;
    float result = count * calculaton;
    Serial.println(result);
    Serial.print(fbdo.stringData() + " / ");
    delay(1200);
    lcd.setCursor(0, 1);
    lcd.println(count);
  // Serial.println(count + " / " + fbdo.stringData());
    }
  }
}
