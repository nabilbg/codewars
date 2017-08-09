# -*- coding: utf-8 -*-
"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case

"""
## My Solution
def is_isogram(string):
    #your code here
   return len(string.lower()) == len("".join(set(string.lower())))