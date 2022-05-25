#!/usr/bin/env python

#https://leetcode.com/problems/median-of-two-sorted-arrays/

'''
Median of Two Sorted Arrays
Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.



Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106



'''

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        len_n1 = len(nums1)
        len_n2 = len(nums2)
        if len_n1 == len_n2 == 0:
            return None
        if len_n1 == 0: #NO ELEMENTS IN LIST 1
            if len_n2 % 2 == 0: #EVEN
                return (nums2[int(len_n2/2)]+nums2[int(len_n2/2)-1])/2
            else:
                return nums2[int(len_n2/2)]

        if len_n2 == 0: #NO ELEMENTS IN LIST 2
            if len_n1 % 2 == 0: #EVEN
                return (nums1[int(len_n1/2)]+nums1[int(len_n1/2)-1])/2
            else:
                return nums1[int(len_n1/2)]

        nums = nums1 + nums2

        nums.sort()

        length = len_n1+len_n2

        if length % 2 == 0: #EVEN
            return (nums[int(length/2)] + nums[int(length/2)-1])/2

        return nums[int(length/2)]

obj = Solution()

print(obj.findMedianSortedArrays([1, 2, 5], [3,4]))

print(obj.findMedianSortedArrays([1, 2], [3,4]))

print(obj.findMedianSortedArrays([], []))

print(obj.findMedianSortedArrays([1], [0]))



