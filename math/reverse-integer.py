#!/usr/bin/env python

#https://leetcode.com/problems/reverse-integer/
'''

Reverse Integer
Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21



Constraints:

    -231 <= x <= 231 - 1

Runtime: 63 ms, faster than 13.72% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.7 MB, less than 97.41% of Python3 online submissions for Reverse Integer.

'''

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        tmp = str(x)[::-1]

        x = int(tmp)*sign

        if x >= 2147483647 or x < -2147483648:
            return 0
        return x


obj = Solution()

print(obj.reverse(123))
print(obj.reverse(-123))
