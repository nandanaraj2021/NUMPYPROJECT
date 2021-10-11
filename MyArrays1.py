import numpy as np
import random


arr01 = np.array([[1,2,3],
                [4,5,6]]) #we have 2 rows and 3 columns here --> each value separated by a comma is one row

arr02 = np.array([0.0, 0.1, 0.2, 0.3, 0.4]) 

for row in arr01:
    print(row)
    for col in row: #goes through each element in the row
        print(col,end= ' ')
    print()


for i in arr01.flat:    #no longer in columns and rows
    print(i)



arr03 = np.zeros(5)


arr04 = np.ones((2,4), dtype=int)   #we want an array of 2 rows and 4 columns


arr05 = np.full((3,5), 13)  #3 rows, 5 columns

#EXERCISE
#############

# create a 2 dimensional array of 5 integer elements each using the random module
# and list comprehension

#this is the "range" function in numpy
arr06 = np.arange(5)

arr07 = np.arange(5, 10)

arr08 = np.arange(10, 1, -2)

arr09 = np.linspace(0.0, 1.0, num=5)

arr10 = np.arrange(1,21).reshape(4,10)


print()