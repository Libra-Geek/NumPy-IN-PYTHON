import numpy as np

#learn how to load and save arrays in your project
#saving single arrays
arr = np.arange (10)
print(arr)

np.save('saved_array', arr)
#In this argument of np.saved, the first value is the filings while the second is the array we actually want to interact with
#np.save is used to save the array we already have
#New File is created  - saved_array.npy

#np.load is the function used to load our array back
new_array = np.load('saved_array.npy')
print (new_array)

#saving multiple arrays
array1 = np.arange(25)
array2 = np.arange(30)
#to compress these arrays into one, we need to use the Save or savez funtion
#the save function is used for storing single arrays while the savez function is used for storing multiple arrays
np.savez('saved_archive.npz',x= array1, y= array2)
load_archive =np.load('saved_archive.npz')
print ('load_archive[x] is')
print (load_archive['x'])
print('load_archive[y] is')
print (load_archive ['y'])

#how to save your codes to a txt.file
np.savetxt('notepadfile.txt',array1,delimiter=',')
#the delimiter is used to separate the parts or content of the array

#loading of txt files
load_txt_file = np.loadtxt('notepadfile.txt', delimiter=',')
print("load_txt_file is")
print (load_txt_file)
