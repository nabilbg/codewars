# -*- coding: utf-8 -*-
"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.

"""
# My solution
def accum(s): 
    iteration = 0
    string = ''
    for each in list(s):
        string += each.upper()
        for _ in range(iteration):
            string += each.lower()
        string += '-'
        iteration +=1
    return string[:-1]


#Clever Solutions

def accum(s):
    str = ""
    for i in range(0, len(s)):
        str += s[i].upper()
        str += s[i].lower()*i
        if i != len(s)-1:
            str += "-"
    return str


def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))



    
        

