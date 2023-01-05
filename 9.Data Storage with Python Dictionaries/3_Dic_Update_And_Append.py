# -*- coding: utf-8 -*-
"""
Spyder Editor
 
"""

db = {} 


db["names"]= "MrHamsho"
db["age"]= 29

db.update({"names":["John","mrHamsho"]})
db.update({"age":[27,29]})

db["names"].append("Kate")
db["age"].append(23)

 
print(db)

