from typing import *

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    i=1
    ls=[]
    fact=factorial(i)
    while fact<=n:
        ls.append(fact)
        i+=1
        fact=factorial(i)
    return ls

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)