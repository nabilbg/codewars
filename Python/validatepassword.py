# -*- coding: utf-8 -*-
"""
You need to write regex that will validate a password to make sure it meets the following criteria:

    At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number

Valid passwords will only be alphanumeric characters.

"""

import re
regex= re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{6,}$')



"""
    
    (?=.*?\d) Checks for atleast one digit
    (?=.*?[A-Z]) Atleast one uppercsae.
    (?=.*?[a-z]) Atleast one lowercase.
    [A-Za-z\d]{6,} Matches uppercase or lowercase or digit characters 6 or more times. 
    This ensures that the match must have atleast 10 characters.
"""
