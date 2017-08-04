# -*- coding: utf-8 -*-
"""
The goal of this exercise is to convert
 a string to a new string where each character
 in the new string is '(' 
 if that character appears only once in the original string,
 or ')' if that character appears more than once in 
 the original string. Ignore capitalization when determining
 if a character is a duplicate.

Examples:

"din" => "((("

"recede" => "()()()"

"Success" => ")())())"

"(( @" => "))(("

"""

#My solution
def duplicate_encode(w):
    #your code here
    word_count={}
    string = ""
    for word in w.lower():
      if word not in word_count:
           word_count[word] = 1
      else:
           word_count[word] += 1
    for k in w.lower():
        if word_count[k] == 1:
           string += '('
        else:
            string += ')'
    return string

# Best Practices

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])



from collections import Counter
def duplicate_encode(word):
    word = word.lower()
    counter = Counter(word)
    return ''.join(('(' if counter[c] == 1 else ')') for c in word)


       
   