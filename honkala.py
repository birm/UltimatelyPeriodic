import time # for benchmark
"""
No noted implementation guidance beyond brute force-finding index.

Relevant Lemmas

Lemma 2: Number of states can map to periodicity

Lemma 9: bounds on size of index

Theorem 1:
recognizable = ultimately periodic, and specify that the below works

"""

# input: k-automata output
# pick an index I
# construct lam_n(L), check finite number of times if recognizable

# representation functions from paper
def lam(k, w):
    sum = 0
    for i in range(len(w)):
        sum += w[i] * k**(len(w)-i-1)
    return sum

def v(k, w):
    sum = 0
    for i in range(len(w)):
        sum += w[i] * k**i
    return sum

# however, for our purposes, we need a stringy representation function emulating l(k,w)
def stringylam(k, w):
    # coerce into base k (careful!)
    return "//".join([str(x%k) for x in w])


def procedure(k, input, I):
    index = input[:I]
    period = input[I:]
    # is it periodic?
    for i in range(1, int(I/2) + 1):
        # ignore "overflow" for finite case
        match = stringylam(k,period[:i])
        idx = len(period) - (len(period) % i)
        working = stringylam(k, period[:idx])
        # use string replace to check periodicity of given order
        if len(working.replace(match, "").replace("//", "")) == 0:
            pass
            return i # this is a minimal period given index I
    return False # failed for I

# test by running python honkala.py from this dir

if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7]
    stringylam(10, input)

    m = 16

    def transition1(q, i, k=10):
        # return (((i[0] % 123) * (q % 131)) + (i[0] % 123))%k
        return ((((i[0] % 2473)+1) * (q % 3847)))%k + 1

    numbers = range(1, int(m) + 1)

    # get input
    input = []
    q = 1
    for i in range(m):
        q = transition1(q, [numbers[i]])
        input.append(q)

    for i in range(m):
        procedure(10, input, i)

    # benchmark time!
    for j in range(13, 22):
        m = 2**j
        start = time.process_time()
        numbers = range(1, int(m) + 1)
        # get dfao output as input
        input = []
        q = 1
        for i in range(m):
            q = transition1(q, [numbers[i]])
            input.append(q)
        for i in range(m):
            procedure(10, input, i)
            if (i%200==0):
                print(i, time.process_time() - start)
        print(m, ",",time.process_time() - start)
