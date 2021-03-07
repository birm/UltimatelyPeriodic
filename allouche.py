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



def makeM1(DFAO, I, N,P):
    k = 10 # base
    q0p = ("=", 0, DFAO.q0, DFAO.q0, I[0], N[0], P[0])

    def Fp(state):
        (b, c, q, r) = state
        return not(b == "<" or q == r)

    def delP(state, inputs):
        (b, c, q, r) = state
        i, n, p = inputs
        b1 = u(b, i, n)
        i1 = math.floor((i+p+c)/k)
        q1 = DFAO.d(q, i)
        r1 = DFAO.d(r, (i+p+c)%k)
        return (b1, i1, q1, r1)

    return Automaton.Automaton(delP, q0p, Fp, inputs=[I,N,P])

def makeM2():
    # powerset construction
    pass

def makeM3():
    pass
