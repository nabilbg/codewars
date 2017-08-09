# -*- coding: utf-8 -*-
"""
Instructions

Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.
Example

Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );

"""

## My Solution
import re
def capitals(word):
    #your code here
    return [i  for i in range(len(word)) if re.search('[A-Z]', word[i])]


## Best Practices
def capitals(word):
    return [i for (i, c) in enumerate(word) if c.isupper()]

def capitals(word):
    return filter(lambda x: word[x].isupper(), range(len(word)))