# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
state=1
while(1):
    transit = input("Enter a Letter: ")
    print("You have entered", state)
    
    if state == 1:
        if transit == 'W':
            state = 2
    
    elif state == 2:
        
        if transit == 'G':
            state= 3
            
        elif transit == 'S':
            state=1
     
    elif state == 3:
        if transit == 'L':
            state=1
    print("Right Now you are in state:", state)
        
    
    
    
    
    