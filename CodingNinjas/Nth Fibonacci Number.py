from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def fibonacci(n):
    n=int(n)
    if n in map_fib:
        return map_fib[n]
    
    val=fibonacci(n-1)+fibonacci(n-2)
    map_fib[n]=val
    return val

map_fib={
    1:1,
    2:1
}
print(fibonacci(input()))