import os

chars = input("Input character to multiply: ")
amount = int(input("Input how many times to multiply: "))
file = input("Input the file to save to: ") 


write_file = open(file, 'w')
write_chars = chars * amount

for line in write_chars:
    write_file.write(line)
write_file.close()

