from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

n=int(input())
if n<=2:
    print(1)
else:
    val1=1
    val2=1
    for i in range(n-2):
        val3=val1+val2
        val1=val2
        val2=val3
    print(val3)