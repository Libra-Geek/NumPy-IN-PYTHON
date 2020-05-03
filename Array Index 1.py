import numpy as np
array = np.arange (0,12)
print (array)

#element of the array
print(array[0])

#2nd element - array1
#3rd element - array2

#indexing
print (array[0:5])
print (array[2:6])
array[0:5] = 20 #to change the values in the indexes 0-5 to 20 and leave the rest the way they were
print (array)

#Interesting and Important
array2 = array[0:6]
print (array2)
array2[:] = 29 #[:] means that all elements are modified
print (array2)
print (array)
#array2 was created from array1 and this makes it less complicated to operate

#creating new array copy
arraycopy = array.copy()
print (arraycopy)
