#include <Face.h>
#include <LEDMatrix.h>

#define WS2812_pin 8 // only digital pin 8 works right now!
#define numberOfLEDs 256// total number of RGB LEDs

Face myFace(8);

void setup() {
  //Set up hardware
  pinMode(WS2812_pin, OUTPUT);

  //create a new Face object on pin 8 
  Face myFace(WS2812_pin);  
  Serial.begin(9600);  // start serial communication at 9600 baud
}
void loop() {
   // Read and execute commands from serial port
   if (Serial.available()) {  // check for incoming serial data
      String command = Serial.readString();  // read command from serial port
      if (command == "loading") {  // turn on LED
         myFace.loading(); 
         myFace.loading(); 
         myFace.loading();
      } else if (command == "happy") {  // turn off LED
         myFace.startup(); 
         myFace.happy_standby(); 
         myFace.happy_standby(); 
      } else if (command == "angry") {  // read and send A0 analog value
         myFace.angry_transition(); 
         myFace.angry_standby();
         myFace.angry_standby();
         myFace.angry_transition_reverse();
         myFace.happy_standby();
      }
   }
}
