#!/usr/bin/env python

#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]

 

Constraints:

    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9'].


2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz
0 -> N/A

Runtime: 40 ms, faster than 58.08% of Python3 online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.9 MB, less than 78.13% of Python3 online submissions for Letter Combinations of a Phone Number.

'''

dig_map = {}
dig_map['2'] = ['a', 'b', 'c']
dig_map['3'] = ['d', 'e', 'f']
dig_map['4'] = ['g', 'h', 'i']
dig_map['5'] = ['j', 'k', 'l']
dig_map['6'] = ['m', 'n', 'o']
dig_map['7'] = ['p', 'q', 'r', 's']
dig_map['8'] = ['t', 'u', 'v']
dig_map['9'] = ['w', 'x', 'y', 'z']

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        strings = []

        for digit in digits:
            if len(strings) == 0:
                strings = dig_map[digit]
            else:
                tmp_strings = []
                for string in strings:
                    for d in dig_map[digit]:
                        tmp_strings.append(string + d)
                strings = tmp_strings

        return strings


obj = Solution()

print(obj.letterCombinations("23"))
print(obj.letterCombinations("2"))
print(obj.letterCombinations(""))