from math import sqrt

n=int(input())

if n==1:
    print("NO")
else:
    flag=True
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            flag=False

    if flag:
        print("YES")
    else:
        print("NO")