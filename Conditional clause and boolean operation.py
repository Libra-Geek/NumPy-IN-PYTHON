import numpy as np

x = np.array ([100,400,500,600]) #each member of array x as 'a'
y = np.array ([10,15,20,25]) #each member of array y as 'b'
condition = np.array([True,True,False,False])

#use loops directly to perform this
z = [a if cond else b for a, cond, b in zip(x,condition,y)]
#the above formula simply states that if any element of x meets the condition, the value should be inputed, if false, put 'y'
print (z)

#np.where (#condition, #value for yes, #value for no)
z2 = np.where (condition, x ,y)
print (z2)
z3 = np.where (x>0, 0,1) #where the value of x>0, replace with 0, if not replace with 1
print (z3)

#Standard functions of numpy

#sumx
print (x.sum())

n= np.array([[1,2],[3,4]])
#columnsumx
print (n.sum(0))

#meanx
print (x.mean())

#standard deviation
print (x.std())

#variance
print (x.var())

#logical operations - and/or operations
condition2 = np.array([True,False,True])
print (condition2.any()) #or operator
print (condition2.all()) #and operator

#sorting in numpy arrays
unsortedarray = np.array([1,2,8,10,7,3])
unsortedarray.sort()
print (unsortedarray)
arr2 = np.array (['solid', 'solid', 'solid', 'liquid', 'liquid', 'gas', 'gas'])
print (np.unique (arr2))

#inland dimension
print(np.in1d(['solid', 'gas', 'plasma'], arr2))


