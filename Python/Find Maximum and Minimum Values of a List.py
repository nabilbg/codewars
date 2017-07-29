# -*- coding: utf-8 -*-
"""
KATA - Find Maximum and Minimum Values of a List



"""
#MY SOLUTION
def min(arr):
    #your code here...
    arr.sort()
    return arr[0]

def max(arr):
    #...and here
    arr.sort()
    return arr[-1]

#CLEVER SOLUTION
def min(arr):
    return sorted(arr)[0]

def max(arr):
    return sorted(arr)[-1]