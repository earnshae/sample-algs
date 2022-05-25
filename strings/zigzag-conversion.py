#!/usr/bin/env python

#https://leetcode.com/problems/zigzag-conversion/

'''
6. Zigzag Conversion
Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);



Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"



Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000


'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        #THIS SPECIAL HANDLING ACTUALLY IMPROVES SPEED TO BE BETTER THEN 80.89% OF OTHER SOLUTIONS (63ms) and MEMORY USGAE 13.9 MB LESS THEN 76.65%
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[0::2]+s[1::2]

        rows = ["" for i in range(0, numRows)]

        i = 0
        count_up = True
        for c in s:

            rows[i] += c

            if count_up:
                i+=1
                if i == numRows:
                    count_up = False
                    i-=2
            else : #count_down
                if i == 1:
                    i = 0
                    count_up = True
                else:
                    i -= 1

        return ''.join(rows)

obj = Solution()

print(obj.convert("PAYPALISHIRING", 4))
print(obj.convert("PAYPALISHIRING", 3))
print(obj.convert("ABC", 1))
print(obj.convert("ABCDEF", 2))
