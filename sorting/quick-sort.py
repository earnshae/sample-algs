#!/usr/bin/env python

# Python quicksort algorithm

# Just a little refresher on the quick sort algorithm

# Quick sort is a recursive sorting algorithm, using a divide and conquer strategy.

# I take no credit for originality of the code.
# My main purpose here was working through the algorithm to refresh my memory.
# Here are the references I studied:

# Refs :
# https://en.wikipedia.org/wiki/Quicksort
# https://www.geeksforgeeks.org/python-program-for-quicksort/

def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        partitioning_index = partition(l, r, nums)
        quicksort(l, partitioning_index-1, nums)
        quicksort(partitioning_index+1, r, nums)
    return nums

example = [2, 5, 6, 1, 4, 6, 2, 4, 7, 8]

print(quicksort(0, len(example)-1, example))
