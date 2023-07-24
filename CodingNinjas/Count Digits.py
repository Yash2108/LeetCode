def countDigits(n: int) -> int:
    str_n=str(n)
    ls=[]
    for i in str_n:
        if i=='0':
            continue
        if n%int(i)==0:
            ls.append(i)
    return len(ls)