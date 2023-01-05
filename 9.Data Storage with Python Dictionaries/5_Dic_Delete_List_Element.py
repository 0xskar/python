# -*- coding: utf-8 -*-
"""
Spyder Editor
 
"""

db = {} 
 

db.update({"names":["John","mrHamsho"]})
db.update({"age":[27,29]})

index= db["names"].index("John")

del db["names"][index]
del db["age"][index]

 
print(db)

