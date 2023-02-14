import numpy as np

# populate arrays with specific numbers the following is an 8 element array
one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

# np.array to create two-dimensional array. We use and extra later of square brackets. example 3x2 array
two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

# To populate an array with all zeroes, call np.zeros. To populate an array with all ones, call np.ones.

# Populate arrays with sequences of numbers with np.arange
sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

# Populate arrays with random numbers with np.random.randint The following call populates a 6-element array with random integers between 50 and 100. 
random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)

# random 
random_floats_between_0_and_1 = np.random.random([6])
print(random_floats_between_0_and_1) 

# if we want to add or subtract two arrays linear algebra needs two operands to have the same dimensions. use broadcasting to add 2.0 to the value of every item in the array of the previous cell.
random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

# The follow operation uses broadcasting to multiply each cell by 3
random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

#task 1 problemset
print('task 1 problemset')
feature = np.arange(6, 21)
print(feature)
label = (3 * feature) + 4
print(label)