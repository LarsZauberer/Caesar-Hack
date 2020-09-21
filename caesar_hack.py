from letter import letter
import logging
log = logging.getLogger("Caesar Hack")


class caesar_hack:
    def __init__(self, code: str, alphabet="abcdefghijklmnopqrstuvwxyz",
                 many_char="enisratdhulcgmobwfkzpvjyxq"):
        log.debug(f"Checking the arguments: {code}, {alphabet}, {many_char}")
        assert type(code) == str
        assert type(alphabet) == str
        assert type(many_char) == str
        assert len(alphabet) == len(many_char)
        log.debug(f"Assigning the arguments")
        self.code = code.lower()
        self.alphabet = alphabet.lower()
        self.many_char = list(many_char.lower())
        self.sort_counts = []
        self.letters = []
        self.finished = []

    def count_and_sort(self):
        """Count and sort the letters in the code
        """
        counts = {}
        for item in self.alphabet:
            counts[item] = self.code.count(item)
        self.sort_counts = sorted(counts.items(),
                                  key=lambda x: x[1],
                                  reverse=True)
        log.debug(f"Sorted and counted letters: {self.sort_counts}")

    def add_letters(self):
        """Adds the letter obj to the letters
        """
        for i in self.sort_counts:
            self.letters.append(letter(i[0], self))

    def calc_most_used_possibilities(self):
        """Calculates the possibilities of the letters
        """
        max_value = self.sort_counts[0][1]
        max_values_length = [x for x in self.sort_counts if x[1] == max_value]
        max_values_length = len(max_values_length)
        log.debug(f"Max Value Length: {max_values_length}")
        for i in range(max_values_length):
            # Calculating the possibilities of the letters and adding
            # them to finished
            self.sort_counts.pop(0)
            self.letters[0].add_possibilities(max_values_length)
            self.finished.append(self.letters[0])
            self.letters.pop(0)
        for i in range(max_values_length):
            self.many_char.pop(0)
        log.debug(f"Shortened common letters: {self.many_char}")

    @property
    def keys(self):
        """Generates a list of all possible keys

        Returns:
            list: all possible keys
        """
        for i in self.finished:
            i.add_key_possibilities()
        self.keys_list = []
        for i in self.finished:
            for e in i.key_possibilities:
                self.keys_list.append(e)
        log.debug(f"Key List: {self.keys_list}")
        return self.keys_list

    @property
    def key(self):
        """Generates the final keys

        Returns:
            set: Final keys for decryption
        """
        key = set({})
        max_value = 0
        keys = self.keys
        for i in keys:
            if keys.count(i) > max_value:
                max_value = keys.count(i)
        for i in keys:
            if keys.count(i) == max_value:
                key.add(i)
        log.debug(f"Set of keys found: {key}")
        return key

    def run(self):
        """Hacks the code in one go

        Returns:
            set: The final key for decryption
        """
        self.count_and_sort()
        self.add_letters()
        while len(self.letters) != 0:
            self.calc_most_used_possibilities()
        return self.key
