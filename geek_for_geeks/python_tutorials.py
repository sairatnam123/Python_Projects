"""python tutorials practice"""

import sys
import keyword
import operator
from datetime import datetime
import os

#keyword: it is a library that are reserved keywords not used an identifiers
keyword_list=keyword.kwlist
print(keyword_list)
print("length of keywords",len(keyword_list))
#identifiers are the names given to entities like class, functions, variables ..etc It helps to define one entity to another entity
#identifiers cannot start with digits and doesn't use any special symbols
#keywords cannot use as an identifiers
variable_1=10
print(variable_1)
#comments --single line comments are begin with hashtag and multiple lines are use as triple quotations
#statements --the interpreter can execute the instructions
p=10+20
print("expression",p)
#multiple line statements
ex=10\
    +\
    20
print("multiline expression",ex)
#indentation means it is space at the beginning in code it refers to block of code in a python
def function():
    sum_=5+2
    return sum_
print("indentation is represented in python",function())

