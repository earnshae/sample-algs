#!/usr/bin/env python

# https://leetcode.com/problems/longest-palindromic-substring/

'''

Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

'''

#so we previously wrote an is palindrome function

# So we just need to got through substrings of the string looking for sub palindroms

'''

Too slow

def is_palindrome(s):
    s = s.lower()
    # of length 0/1 are palindromes by default

    if len(s) < 2:
        return True

    return s == s[::-1]

def find_longest_palandrome(s):
    # I am thinking recursion. of sub strings
    def is_palindrome(s):
        s = s.lower()
        # of length 0/1 are palindromes by default

        if len(s) < 2:
            return True

        return s == s[::-1]

    if is_palindrome(s):
        return s

    s0 = find_longest_palandrome(s[:-1])
    s1 = find_longest_palandrome(s[1:])

    if len(s0) >= len(s1):
        return s0

    return s1
'''
class Solution(object):
    def find_longest_palindrome(self, s):
        l = len(s)
        # create an l x l matrix with all values = False
        matrix = [[False for i in range(l)] for i in range(l)]

        # set the diagonal = True
        for i in range(l):
            matrix[i][i] = True

        max_length = 1

        start = 0

        for j in range(2, l+1):
            for i in range(l- j+1):
                end = i+j
                if j ==2:
                    if s[i] == s[end-1]:
                        matrix[i][end-1]=True
                        max_length=j
                        start=i
                else:
                    if s[i] == s[end-1] and matrix[i+1][end-2]:
                        matrix[i][end-1]=True
                        max_length=j
                        start=i

        return s[start:start+max_length]

obj = Solution()
print(obj.find_longest_palindrome("abbcccbbbcaaccbababcbcabca"))
#result bbcccbb

    #find_longest_palandrome()