from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    hashtable={i:0 for i in range(1, m+1)}
    for i in edges:
        hashtable[i]+=1
    if n<m:
        return [i for i in hashtable.values()][:n]
    else:
        return [i for i in hashtable.values()]