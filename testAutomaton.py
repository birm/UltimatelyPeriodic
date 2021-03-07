# A very obviously repeating automata
import Automaton
import random

def basicd(n):
    n +=1
    return n%4

def acceptingF():
    return True

simple = Automaton.Automaton(basicd, 1, acceptingF)

for i in range(100):
    print(repr(next(simple)))


# A very obviously repeating automata with input

numbers = [random.randint(0,4) for x in range(100)]

def inputd(n, i):
    n += i[0]
    return n%4

withinput = Automaton.Automaton(inputd, 1, acceptingF, inputs=[numbers])

for i in range(100):
    print(repr(next(withinput)))
