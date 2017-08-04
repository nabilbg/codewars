# -*- coding: utf-8 -*-
"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number.


"""
# My Solution
def multiply(num):
    result = 1
    k = [int(x) for x in str(num)]
    for i in k:
        result *= i
    return result

def persistence(num):
  count = 0
  while(len(str(num)) > 1):
      num = multiply(num)
      count += 1
  return count



# Clever Solutions
def persistence(n, result=0):
    if len(str(n)) == 1:
        return result
    else:
        return persistence(reduce(lambda x, y: int(x) * int(y), str(n), 1), result + 1)
    
persistence = lambda n: 0 if n < 10 else persistence(reduce(lambda a, b: a*int(b), str(n), 1)) + 1

    