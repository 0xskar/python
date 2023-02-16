# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

total_height = 0
heights = 0

for height in student_heights:
    total_height += height
    heights += 1

average_height = total_height / heights

print(f"Total height is {total_height}, and average Height is {average_height.__round__()}.")