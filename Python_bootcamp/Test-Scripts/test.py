# string1 = "Linux"
# string2 = "Hint"
# joined_string = string1 + string2
# print(joined_string)

#Let's try loading a csv file
# import os
# import pandas
# # os.chdir('/Users/bknorris/Documents/Scripts/Python/Python_bootcamp/Test-Scripts/') #change directory
# directory = '/Users/bknorris/Documents/Scripts/Python/Python_bootcamp/Test-Scripts/'
# fileName = 'TestCSV.csv'
# data = pandas.read_csv(directory + fileName)
# print(data)

import numpy as np
data = np.array([['x','','x'],['o','','x'],['x','o','x']])
print(data[[0,2],[2,0]])