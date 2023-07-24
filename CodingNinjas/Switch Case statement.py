from typing import *
from math import pi

def areaSwitchCase(ch: int, a: List[float]):
    # Write your code here
    if ch==1:
        return '{0:.5f}'.format((float(a[0])**2)*pi)
    elif ch==2:
        return '{0:.5f}'.format(float(a[0])*float(a[1]))