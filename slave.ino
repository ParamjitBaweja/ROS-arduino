#include <Wire.h>
int ledpin=13;
int initial=0;
void setup() {
  pinMode(ledpin,OUTPUT);
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(9600);           // start serial for output
}

void loop() {
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {
  while (Wire.available()==0);  // loop through all but the last
    int c = Wire.read();
    if(c==1 && initial==0)
    {
      //Serial.println(c);
      digitalWrite(ledpin,HIGH);
      initial=1;
    }
    else if(c==0 && initial==1)
    {
      //Serial.println(
      digitalWrite(ledpin,LOW);
      initial=0;
    }
  
 // int x = Wire.read();    // receive byte as an integer
  //Serial.println(x);         // print the integer
}
