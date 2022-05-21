#!/usr/bin/env python

# the idea here is find all the element that are greater then the value of the indexed element i and move them ahead
# then put the value at the location of the sub array (move and insert)

# I confess I looked this one up:
# Reference :
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/?ref=lbp
def insertionsort(arr):

    for i in range(1, len(arr)) :
        value = arr[i]
        j = i-1
        while j >= 0 and value < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = value
    return arr

arr = [899, 123, 456, 56, 2, 789, 1000, 11, 989]

print(insertionsort(arr))