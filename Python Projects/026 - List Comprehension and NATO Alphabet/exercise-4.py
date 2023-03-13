sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
# TODO create dictionary called result that takes each word in sentence and calculates
#  the number of letters in each word.
# Write your code below:

result = {word:len(word) for word in sentence.split()}


print(result)
