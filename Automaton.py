class Automaton:
    def __init__(self, d, q0, F, inputs=False):
        # self.Q = Q # states, !! I don't think I need this
        # self.S = S # alphabet, !! I don't think I need this
        self.d = d # transition function
        self.q0 = q0 # initial state
        self.F = F # accept state check
        self.q = [q0] # assign initial state
        self.inputs = inputs

    def __repr__(self):
        return str(self.q[-1]) + ": n=" + str(len(self.q)-1) # I think we care about current state in a repr?

    def __iter__(self):
        return self

    def __next__(self):
        n = len(self.q) - 1
        if self.inputs:
            self.q.append(self.d(self.q[-1], [i[n] for i in self.inputs]))
        else:
            self.q.append(self.d(self.q[-1]))
        return self.q[-1]

    def accept(self, n):
        for i in range(n):
            next(self)
        return F(self.q[-1])

    def reset(self):
        self.q = [self.q0]
