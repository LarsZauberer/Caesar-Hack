import logging
log = logging.getLogger("Letter")


class letter:
    def __init__(self, char: str, hack):
        """One Letter of the encrypted message

        Args:
            char (str): the char
            hack (caesar_hack): the main hack object
        """
        from caesar_hack import caesar_hack
        log.debug(f"Checking the arguments {char}, {hack}")
        assert type(char) == str
        assert type(hack) == caesar_hack
        log.debug(f"Assigning the aruments")
        self.char = char
        self.hack = hack
        self.possibilities = []
        self.key_possibilities = []

    def add_possibilities(self, others):
        """Calculates the possible letters

        Args:
            others (int): How many other letters with the same count
        """
        assert type(others) == int
        for i in range(others):
            self.possibilities.append(self.hack.many_char[i])

    def add_key_possibilities(self):
        """Calculates the possible keys
        """
        for i in self.possibilities:
            dif = self.get_index(self.char) - self.get_index(i)
            self.key_possibilities.append(dif % len(self.hack.alphabet))

    def get_index(self, char):
        """Converts a char to the corresponding index in the alphabet

        Args:
            char (str): char to be converted

        Returns:
            int: converted char to the corresponding index in the alphabet
        """
        for index, item in enumerate(self.hack.alphabet):
            if item == char:
                return index
