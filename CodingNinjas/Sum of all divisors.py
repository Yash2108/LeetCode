from math import sqrt, ceil

def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    divisor_sum=0
    if n==1:
        return 1

    for i in range(1, int(sqrt(n))+1):
        if n%i==0:
            divisor_sum+=i
            if i != n/i:
                divisor_sum+=int(n/i)

    return divisor_sum+sumOfAllDivisors(n-1)