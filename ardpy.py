#!/usr/bin/env python3
import serial #for Serial communication
import time   #for delay functions
 
ArduinoSerial = serial.Serial('/dev/ttyACM1',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print (ArduinoSerial.readline()) #read the serial data and print it as line
print ("Enter 1 to get LED ON & 0 to get OFF")

 
while 1:      #Do this in loop
    print("input\n")
    #var = raw_input() #get input from user
    var=int(input())
    print("you just entered:")
    print(var)
    
    if (var == 1): #if the value is 1
        ArduinoSerial.write(1) #send 1
        print ("LED turned ON")
        print (ArduinoSerial.readline())
        time.sleep(1)
    
    if (var == 0): #if the value is 0
        ArduinoSerial.write(var) #send 0
        print ("LED turned OFF")
        print (ArduinoSerial.readline())
        time.sleep(1)
