# -*- coding: utf-8 -*-
"""
Spyder Editor
 
"""

db = {} 
 

db.update({"names":["John","mrHamsho"]})
db.update({"age":[27,29]})

index= db["names"].index("John")


for value in db.values():
    for subvalue in value:
        print(subvalue)


#for key in db.keys():
#    del db[key][index]
 
 
