file = open("my_data.txt")
contents = file.read()
print(contents)
file.close()


with open("cool_data.txt", mode="a") as file:
    stuff = file.write("\nNo, My name is Errol.")
