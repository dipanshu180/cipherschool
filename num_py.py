# numpy - Numerical python

# more efficcient and provide better performance for nunmerical operation copared to python built in list

# array object in numpy is called ndarray

import numpy as np

# creating a 1D array from a list
arr1 = np.array([[1,2,3,4,5]])
print(arr1)

print(arr1+1)
print("\n")
# 2D array

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)


#zeroes

zero = np.zeros((3,4))
print(zero)
print("\n")
one = np.ones((3,4))
print(one)


#Range

ran = np.arange(10,20,2)
print(ran)

#RAndom
random = np.random.rand(3,3)
print(random)

# Basic operation

sq = np.sqrt(arr1)
print(sq) #square root

print(np.exp(arr1))
print(np.log(arr1))

#Index Slicing

print(arr1[0])
print(arr1[-1])

#Reshaping and Transposing

reshaped = arr1.reshape((3,2))
print(reshaped) 


