def calcGDC(n:int, m: int) -> int:
    # Write your code here

    if n==m:
        return n
    elif n==1 or m==1:
        return 1
    elif n==0:
        return m
    elif m==0:
        return n

    return calcGDC(min(n, m), max(n ,m)%min(n, m))