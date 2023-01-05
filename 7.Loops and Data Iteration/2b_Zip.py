# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 21:04:35 2022

@author: Hamsho
"""
 
shapes = ["Square", "Circle","Triangle"]
centers = [ (10,10), (50,50),(100,100)]
colors = ["Red","Blue","Yellow"]

#for i in range(0, len(shapes)):
#    print(shapes[i], centers[i])
    
for shape, center, color in zip(shapes, centers, colors):
    print(shape,center, color)