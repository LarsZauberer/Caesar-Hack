class letter:
    def __init__(self, char, count, hack):
        self.char = char
        self.count = count
        self.hack = hack
        self.possibilities = []
        self.key_possibilities = []

    def add_possibilities(self, others):
        for i in range(others):
            self.possibilities.append(hack.many_char[i])

    def add_key_possibilities(self):
        for i in self.possibilities:
            dif = self.get_index(self.char) - self.get_index(i)
            self.key_possibilities.append(dif % len(hack.alphabet))

    def get_index(self, char):
        for index, item in enumerate(hack.alphabet):
            if item == char:
                return index
