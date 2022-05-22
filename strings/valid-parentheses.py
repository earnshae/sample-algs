#!/usr/bin/env python

#https://leetcode.com/problems/valid-parentheses/

'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.



Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false



Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

Accepted
2,249,248
Submissions
5,504,603
'''

open_pars = ["[", "{", "("]
close_pars = ["]", "}", ")"]

def valid_parentheses(str) :

    stack = []

    for char in str :
        if char in open_pars :
            stack.append(char)

        elif char in close_pars :

            index = close_pars.index(char)

            if len(stack) > 0:
                comp = stack.pop()
                if open_pars[index] != comp:
                    return False
            else:
                return False

    return len(stack) == 0

string = "["
print(string, "-", valid_parentheses(string))

string = "(("
print(string, "-", valid_parentheses(string))

string = "{[]{()}}"
print(string, "-", valid_parentheses(string))

string = "[{}{})(]"
print(string, "-", valid_parentheses(string))

string = "((()"
print(string, "-", valid_parentheses(string))

