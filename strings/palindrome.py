#!/usr/bin/env python

# A simple python script to determine if a word is a palindrome
# You could also do this recursively but... why not take advantage of the easy string ops.

def is_palindrome(s):
    s = s.lower()
    #of length 0/1 are palindromes by default

    if len(s) < 2:
        return True

    reverse = s[::-1]

    return s == reverse

words = ["A", "kayak", "potato"]

for word in words :
    if is_palindrome(word) :
        print(word + " is a palindrome.")
    else :
        print(word + " is not a palindrome.")