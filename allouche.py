import math # for floor
import Automaton # automation representation

# for M1 construction

# sequence partial comparison
def u(flag, i, n):
    if flag == "<":
        return "<" if i <= n else ">"
    elif flag == ">":
        return "<" if i < n else ">"
    elif flag == "=":
        if i == n:
             return "="
        else:
            return "<" if i < n else ">"
    else:
        raise AssertionError("sequence comparison invoked with invalid state (flag)")

# sequence partial add
def pAdd(carry, i, n, k=10):
    if k==0:
        raise AssertionError("sequence addition invoked with invalid base (k)")
    temp = i + n
    temp += carry
    carry = 0
    if temp > k:
        temp -= k*math.floor(temp/k)
        carry = 1
    return (carry, temp)



def M1(DFAO, N,P):
    pass

def M2():
    pass

def M3():
    pass
