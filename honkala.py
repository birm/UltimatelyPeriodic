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
    for i in range(1, len(period)-1):
        # ignore "overflow" for finite case
        match = stringylam(k,period[:i])
        idx = len(period) - (len(period) % len(match))
        working = stringylam(k, period)[:idx]
        # use string replace to check periodicity of given order
        if len(working.replace(match, "").replace("//", "")) == 0:
            return i # this is a minimal period given index I
    return False # failed for I

# test by running python honkala.py from this dir

if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 8, 9, 7, 8, 9, 7]
    stringylam(10, input)
    procedure(10, input, 6)
