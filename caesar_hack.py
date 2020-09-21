from letter import letter
import logging
log = logging.getLogger("Caesar Hack")


class caesar_hack:
    def __init__(self, code, alphabet="abcdefghijklmnopqrstuvwxyz",
                 many_char="enisratdhulcgmobwfkzpvjyxq"):
        assert type(code) == str
        assert type(alphabet) == str
        assert type(many_char) == str
        self.code = code
        self.alphabet = alphabet
        self.many_char = list(many_char)
        self.sort_counts = []
        self.letters = []
        self.finished = []

    def count_and_sort(self):
        counts = {}
        for item in self.alphabet:
            counts[item] = self.code.count(item)
        self.sort_counts = sorted(counts.items(),
                                  key=lambda x: x[1],
                                  reverse=True)

    def add_letters(self):
        self.letters = []
        self.finished = []
        for i in self.sort_counts:
            self.letters.append(letter(i[0], self))

    def calc_most_used_possibilities(self):
        max_value = self.sort_counts[0][1]
        max_values_length = [x for x in self.sort_counts if x[1] == max_value]
        max_values_length = len(max_values_length)
        for i in range(max_values_length):
            self.sort_counts.pop(0)
            self.letters[0].add_possibilities(max_values_length)
            self.finished.append(self.letters[0])
            self.letters.pop(0)
        for i in range(max_values_length):
            self.many_char.pop(0)

    @property
    def keys(self):
        for i in self.finished:
            i.add_key_possibilities()
        self.keys = []
        for i in self.finished:
            for e in i.key_possibilities:
                self.keys.append(e)
        return self.keys

    @property
    def key(self):
        keys = sorted(self.keys, key=lambda x: keys.count(x), reverse=True)
        return keys[0]
