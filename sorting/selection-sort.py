#!/usr/bin/env python

# Didn't need a reference for this one I remember it :) but if you do here is one:
# https://www.geeksforgeeks.org/python-program-for-selection-sort/?ref=lbp
# my solution is pretty close

def selectionsort(arr) :

    for i in range(len(arr)) :

        #find the index of the minimum array i to length of arr
        #start with i as index
        min_index = i
        for j in range(i+1, len(arr)) :
            if arr[min_index] > arr[j] :
                min_index = j

        #swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

arr = [899, 123, 456, 56, 2, 789, 1000, 11, 989]

print(selectionsort(arr))