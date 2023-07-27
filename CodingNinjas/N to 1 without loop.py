from typing import List

def printNos(x: int) -> List[int]:
    # Write your code here
    if x==1:
        return [1]
    return [x]+printNos(x-1)