from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    ls=[]
    for i in range(n):
        ls.append(fibonacci(i))
    return ls

def fibonacci(n):
    if n in map_fib:
        return map_fib[n]
    
    val=fibonacci(n-1)+fibonacci(n-2)
    map_fib[n]=val
    return val

map_fib={
    0:0,
    1:1
}