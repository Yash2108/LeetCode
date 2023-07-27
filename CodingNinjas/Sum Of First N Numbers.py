from typing import List

def sumFirstN(n: int) -> int:
    # Write your code here.
    if n==1:
        return 1
    return n+sumFirstN(n-1)