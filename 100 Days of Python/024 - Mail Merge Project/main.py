with open("./Input/Names/invited_names.txt", mode="r") as names:
    invited_names = names.readlines()
    name_list = []
    for name in invited_names:
        name_list.append(name.strip("\n"))

for name in name_list:
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        custom_letter = letter.read()
        custom_letter = custom_letter.replace("[name]", name)

        file = open(f"./Output/ReadyToSend/{name}.txt", mode="w")
        contents = file.write(custom_letter)
        file.close()


