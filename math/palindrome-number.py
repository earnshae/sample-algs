#!/usr/bin/env python

#https://leetcode.com/problems/palindrome-number/

'''
Palindrome Number
Easy

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?

Runtime: 75 ms, faster than 66.74% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.8 MB, less than 60.11% of Python3 online submissions for Palindrome Number.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Negatives can't be

        if x < 0:
            return False
        if x == 0:
            return True
        #Can't have a leading 0
        if x%10 == 0:
            return False
        rev_x = 0
        tmp = x
        while tmp > 0:
            digit = tmp % 10
            rev_x = 10 * rev_x + digit
            tmp = tmp//10
        return x == rev_x

obj = Solution()

print(obj.isPalindrome(121))
print(obj.isPalindrome(10))
print(obj.isPalindrome(-121))
print(obj.isPalindrome(0))

