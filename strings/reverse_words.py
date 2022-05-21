#!/usr/bin/env python

# A script to reverse the words in a given string

# Force be with you => you with Force be

def reverse_words(s) :
    s = s.lower()

    words = s.split(" ")
    words.reverse()

    return " ".join(words)

strings = ["Force is strong with you", "today is a good day", "Tut Tut it looks like rain"]

for string in strings :
    print(string.capitalize() + ", reversed  is: " + reverse_words(string).capitalize())

