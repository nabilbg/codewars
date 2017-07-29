# -*- coding: utf-8 -*-
"""

Find the stray number

You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Implement the method stray which accepts such array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples:

[1, 1, 2] => 2

[17, 17, 3, 17, 17, 17, 17] => 3


"""

#My solution using  XOR operator ^ is associative and commutative
def stray(arr):
    
    #for index, each in enumerate(arr):
      #  print(each[index])
      result = 0
      for i in arr:
          result ^= i
      return result
# Others solution

def stray(arr):
    """ Return the odd man out integer from the input list """
    
    return [x for x in arr if arr.count(x) == 1][0]

