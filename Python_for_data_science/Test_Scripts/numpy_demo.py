# -*- coding: utf-8 -*-
"""
Demo for numpy from the Python Data Science/Machine Learning
Bootcamp on udemy.com.
"""


import numpy as np

# numpy arrays
my_list = [1,2,3]
array = np.array(my_list)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = np.array(my_mat)

# Create an array in numpy
array = np.arange(0,10,2) #0 to 10 non-inclusive and just even numbers

# Generate zeros
zz = np.zeros((3,3)) #must insert a tuple. This is a 3x3 matrix of zeros.

# Generate ones
ones = np.ones((3,3))

# linspace
lin = np.linspace(0,2.5,10)

# Let's create an identity matrix
iden = np.eye(3)

# Random number generators
rand1d = np.random.rand(5) # 5x1 output
rand2d = np.random.rand(5,5) # 5x5 output
gauss = np.random.randn(2) #two numbers from a gauss dist.
randint = np.random.randint(0,11,3) #3 random numbers from 0 to 10

# Useful attributes of arrays
arr = np.arange(25) # 1D array from 0 to 24
randarr = np.random.randint(0,50,10)
new_arr = arr.reshape(5,5) # reshape
maximum = randarr.max() # returns max of array
minimum = randarr.min() # returns min of array
maxid = randarr.argmax() # returns index of maximum
minid = randarr.argmin() # returns index of minimum
