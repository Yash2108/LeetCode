from typing import *

def dataTypes(input_t: str):
    input_t=input_t.strip()
    if input_t=='Integer':
        return(4)
    elif input_t=='Long':
        return(8)
    elif input_t=='Float':
        return(4)
    elif input_t=='Double':
        return(8)
    elif input_t=='Character':
        return(1)
    else:
        return(input_t)