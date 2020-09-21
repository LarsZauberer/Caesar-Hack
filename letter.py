import logging
log = logging.getLogger("Letter")


class letter:
    def __init__(self, char, hack):
        from caesar_hack import caesar_hack
        assert type(char) == str
        assert type(hack) == caesar_hack
        self.char = char
        self.hack = hack
        self.possibilities = []
        self.key_possibilities = []

    def add_possibilities(self, others):
        assert type(others) == int
        for i in range(others):
            self.possibilities.append(self.hack.many_char[i])

    def add_key_possibilities(self):
        for i in self.possibilities:
            dif = self.get_index(self.char) - self.get_index(i)
            self.key_possibilities.append(dif % len(self.hack.alphabet))

    def get_index(self, char):
        for index, item in enumerate(self.hack.alphabet):
            if item == char:
                return index
