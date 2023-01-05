# -*- coding: utf-8 -*-
"""
Spyder Editor
 
"""

#4px x 4px
# 16px x 16px 

imagePixels = [ 
                [0,0], [1,0], [2,0], [3,0],
                [0,1], [1,1], [2,1], [3,1],
                [0,2], [1,2], [2,2], [3,2],
                [0,3], [1,3], [2,3], [3,3],
            ]

#shift X axis 3 pixles to the right
for i in range(0 , len(imagePixels)):
    imagePixels[i][0]= imagePixels[i][0] + 3

print(imagePixels)

#shift Y axis 2 pixels downwards
for i in range(0 , len(imagePixels)):
    imagePixels[i][1]= imagePixels[i][1] + 2

print(imagePixels)

    
    