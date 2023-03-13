# TODO Create list called results which contains the numbers common in both files,
#  the list should be intergers, not strings. [3, 6, 5, 33, 12, 7, 42, 13]

with open("file1.txt", "r") as file1:
    file1_data = file1.readlines()

with open("file2.txt", "r") as file2:
    file2_data = file2.readlines()

file1_list = [int(line.strip("\n")) for line in file1_data]
file2_list = [int(line.strip("\n")) for line in file2_data]

print(file1_list)
print(file2_list)

results = [number for number in file1_list if number in file2_list]

print(results)
