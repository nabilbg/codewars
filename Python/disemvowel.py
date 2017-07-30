# -*- coding: utf-8 -*-

"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

#My Solution
def disemvowel(string):
   
 ##   return "".join([char if char not in ['a','e','i','o','u'] 
  ##                  else "" for char in string])
    st = ""
    for char in string:
        if char not in  ['a','e','i','o','u','A','E','I','O','U'] :
            st += "".join(char)
        else:
            st += ""
    return st

#refactor

return "".join([char if char not in ['a','e','i','o','u', 'A','E','I','O','U'] 
                    else "" for char in string])

