# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

forwardButton = True

backwardButton = True

#0 : no rotation
#1 : clockwise rotation FW
#2 : anti-clockwise rotation BW

motorStatus = 0

if forwardButton == True:
    motorStatus = 1
    print("Car is moving Forward")

elif backwardButton == True:
    motorStatus = 2
    print("Car is moving Backward")

else:
    motorStatus= 0
    print("Car is not moving")
    
    