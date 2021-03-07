class Automaton:
    def __init__(Q,S,d,q0,T):
        self.Q = Q # states
        self.S = S # alphabet
        self.d = d # transition function
        self.q0 = q0 # initial state
        self.T = T # accept
        self.q = q0 # assign initial state

    def __repr__(self):
        return self.q # I think we care about state in a repr?

class DFA(Automaton):
    def __init__(*args):
        self.type = "Deterministic"
        super(*args)

class NFA(Automaton):
    def __init__(*args):
        self.type = "Non-Deterministic"
        super(*args)
