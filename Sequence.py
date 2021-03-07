class Sequence:
    def __init__(self, value):
        if type(value) is int:
            self.value = reverse([int(d) for d in str(n)])
        else if type(value) is list:
            self.value = value
        else:
            raise AssertionError("Input is not a list or an int")

    def __len__(self):
        return len(self.value)

    # assuming same length
    def __add__(self, other):
        return Sequence([sum(x) for x in zip(self.value, other.value)])

    # assuming same length
    def __lt__(self, other):
        selfVal = reverse(int("".join([str(x) for x in self.value])))
        otherVal = reverse(int("".join([str(x) for x in other.value])))
        return self.value < other.value

    def __getitem__(self, key):
        return self.value[key]
