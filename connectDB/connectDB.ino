/* Documentation firebase library for arduino https://github.com/mobizt/Firebase-Arduino-WiFiNINA for ESP32 
 * 
 * 
 * 
*/

#include "Firebase_Arduino_WiFiNINA.h"

// configure wifi & firebase settings
#define DATABASE_URL "" /
#define DATABASE_SECRET ""
#define WIFI_SSID ""              
#define WIFI_PASSWORD ""       

//Define Firebase data object
FirebaseData fbdo;
int val = 0;

// Setup
void setup()
{
  Serial.begin(115200);
  delay(100);
  Serial.println();
  Serial.print("Connecting to Wi-Fi");
  int status = WL_IDLE_STATUS;
  while (status != WL_CONNECTED)
  {
    status = WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.print(".");
    delay(100);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println("Connected to WiFi");
  Serial.println();

  //Provide the autntication data
  Firebase.begin(DATABASE_URL, DATABASE_SECRET, WIFI_SSID, WIFI_PASSWORD);
  Firebase.reconnectWiFi(true);

  String path = "/km/km";

  Serial.println();

  Serial.println("Getting value from /km/km database... ");
  

  if (Firebase.get(fbdo, path)) {
    Serial.println("km: " + fbdo.stringData());
  }
  else
  {
    Serial.println("error, " + fbdo.errorReason());
  }
}

void loop()
{
}
