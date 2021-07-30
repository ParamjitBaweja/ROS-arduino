# ROS-arduino
Traditionally, ROS-serial is used to communicate between a ros framework, and an ardunio
But, we instead had a python based node connect to the ROS pipeline, and made the node communicate with the arduino using an I2C protocol

The slave.ino program was run on the arduino, this makes use of the wire.h library, and it was then communicated to.
