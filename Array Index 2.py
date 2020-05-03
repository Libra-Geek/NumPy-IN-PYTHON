import numpy as np

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print (arr2d)

#how you can access the rows of the array
print (arr2d[0])
print (arr2d[1])
print (arr2d[2])
print (arr2d[0] [0])
print (arr2d[0] [1])
print (arr2d[0] [2])
print (arr2d[1] [2])

#how to use the column operator to create slices in an index
slice1 = arr2d[0:1,0:2]
print (slice1)
slice2 = arr2d[0:2, 0:2]
print (slice2)

#another type of slicing
slice3 = arr2d[:2, 1:] #this argument is telling numpy to select all data from 0 to 2 and from 1 to the end
print (slice3)

arr2d[:2, 1:] = 15
print (arr2d)

#using loops to index
arr_len = arr2d.shape[0]
for i in range(arr_len):
    arr2d[i] = i;
#print (arr2d) #changing the elements of the array using the loop

#one more way of accesing the rows
print(arr2d[[0,1]])
print(arr2d[[1,2]])
print(arr2d[[1,0]])




