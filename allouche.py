import math # for floor
import Automaton # automation representation
from itertools import chain, combinations
import time # for benchmark

"""
Procedure in a nutshell: create an automata around the given automata,
use powerset construction, use this to determine periodicity
"""

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

# padded representation
def padRep(value, target_length, k=10):
    res = []
    while value>=1 :
        res.append(value % k)
        value -= (value %k)
        value = value / k
    return res + [0] * (target_length - len(res))

def makeM1(k, DFAO, I, N,P):
    q0p = ("=", 0, DFAO.q0, DFAO.q0)

    def Fp(state):
        (b, c, q, r) = state
        return not(b == "<" or q == r)

    def delP(state, inputs):
        (b, c, q, r) = state
        i, n, p = inputs
        b1 = u(b, i, n)
        i1 = math.floor((i+p+c)/k)
        q1 = DFAO.d(q, [i])
        r1 = DFAO.d(r, [(i+p+c)%k])
        return (b1, i1, q1, r1)

    return Automaton.Automaton(delP, q0p, Fp, inputs=[I,N,P])

def makeM2(M1, k=10):
    # subset construction
    res = []
    for j in range(len(M1.q)):
        N = M1.inputs[1]
        P = M1.inputs[2]
        state = M1.q[j]
        tmp = []
        prev_states = set([M1.q[j]])
        # follow possible inputs for each state's i, n, and p values
        for i1 in range(k):
            for i2 in range(k):
                for i3 in range(k):
                        for s in prev_states:
                            tmp.append(M1.d(s, (i1, i2, i3)))
        prev_states |= set(tmp)
        res.append(set(tmp))
    return res

# test by running python allouche.py from this dir

if __name__ == "__main__":

    k = 10
    # Ultimately Periodic, for our test
    def transition1(q, i):
        return (((i[0] % 123) * (q % 131)) + (i[0] % 123))%k

    def F1(q):
        return True

    m = 1e6

    numbers = range(1, int(m) + 1)

    withinput = Automaton.Automaton(transition1, 1, F1, inputs=[numbers])

    for i in range(100):
        next(withinput)

    # without loss of generality, pick I, P
    # iterate through N
    ## FUTURE WORK - use a representation that can work backwards from this
    m = 16
    I_g = padRep(100, m)
    N_g = padRep(23, m)
    P_g = padRep(8, m)

    M1 = makeM1(k, withinput, I_g, N_g, P_g)

    for i in range(m):
        next(M1)

    # M2 runs in O(N**2)
    # print(len([x for x in makeM2(M1)]))

    # benchmark time!
    for j in range(0, 13):
        m= 2**j
        start = time.process_time()
        N_g = padRep(23, m)
        P_g = padRep(8, m)
        I_g = padRep(1, m)
        M1 = makeM1(k, withinput, I_g, N_g, P_g)
        for i in range(m):
            next(M1)
        makeM2(M1)
        print(m, ",",time.process_time() - start)
