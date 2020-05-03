import numpy
print (numpy.array([1,2]))
import numpy as np
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print (my_array1)

#array of two dimensions
my_list2 = [5,6,7,8]
my_array = np.array ([my_list1,my_list2])
print (my_array)

#usage of shape (dimension) function
print (my_array.shape)

#finding out the datatype of the members of the array
print (my_array.dtype)

#zeros, ones, empty function, eye function and arrange
new_array = np.zeros (5) #creates a new numpy array with (1*5). All elements are zero
print (new_array)

new_array = np.ones ([5,5]) #np.ones helps you to get all the elements in an array as 1's
print (new_array)

new_array = np.empty (5)
print (new_array)

new_array = np.eye(5) #the eye function makes all the diagonal elements in an array the same figure (identity matrix)
print (new_array)

new_array = np.arange (5,50,3) #helps to create a progression (arithmetic) where the first argument is the starting number, the second is the final number and the final argument is the difference between the numbers (common difference)
print (new_array)

