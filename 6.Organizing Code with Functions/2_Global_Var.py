
db1=["Echo", "Tiger"]
db2=["Mark", "Lisa"]
db3=["Gary", "Alfa"]


def addToDatabase(name):
    global db1
    global db2
    global db3

    db1.append(name)
    db2.append(name)
    db3.append(name)

addToDatabase("Errol")
addToDatabase("Grant")
addToDatabase("Shnorp")

print("DB 1 is:", db1)
print("DB 2 is:", db2)
print("DB 3 is:", db3)