#!/usr/bin/env python

# Python bubble sort algorithm

# Just a little refresher on the bubble sort algorithm

# I take no credit for originality of the code.
# My main purpose here was working through the algorithm to refresh my memory.
# Here are the references I studied:

# Refs :
# https://www.geeksforgeeks.org/python-program-for-bubble-sort/
# https://en.wikipedia.org/wiki/Bubble_sort

def bubblesort(arr):

    elements = len(arr)
    for i in range(elements-1) :
        for j in range(0, elements-i-1):
            if arr[j] > arr[j+1]:
                #SWAP
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [899, 123, 456, 56, 2, 789, 1000, 11, 989]

print(bubblesort(arr))