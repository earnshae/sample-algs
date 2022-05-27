#!/usr/bin/env python

#https://leetcode.com/problems/longest-common-prefix/

'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

Runtime: 38 ms, faster than 79.21% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 49.92% of Python3 online submissions for Longest Common Prefix.

'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        prefix = ""
        col = 0

        while True:
            c = None
            for str in strs:
                #WE HAVE COMPLETED A STRING
                l = len(str)
                if col > l-1 or l == 0:
                    return prefix
                #FIRST LETTER
                if c == None:
                    c = str[col]
                elif c != str[col]:
                    return prefix
            prefix += c
            col += 1


obj = Solution()

print(obj.longestCommonPrefix(["flower","flow","flight"]))
print(obj.longestCommonPrefix(["dog","racecar","car"]))
print(obj.longestCommonPrefix(["dog"]))
print(obj.longestCommonPrefix(["ab", "a"]))


