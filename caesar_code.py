import logging


class caesar_code:
    def __init__(self, msg: str, key: int):
        self.log = logging.getLogger("Caesar Verschieber")
        self.msg = msg
        self.key = key
        try:
            # Testing the arguments
            self.log.debug("Asserting correct argument types")
            assert type(msg) == str
            assert type(key) == int

            # Alphabet String
            self.alphabet = "abcdefghijklmnopqrstuvwxyz"
            self.log.debug(f"Asserting that the alphabet is 26 characters long")
            assert len(self.alphabet) == 26
        except AssertionError as e:
            # Something went wrong with the assertions
            self.log.error(f"Wrong Argument types or error with the alphabet variable")
            self.log.error(f"{e}")
            raise e
        else:
            self.msg = msg.lower()

    def encrypt(self, key=1):
        if key == 1:
            self.key = abs(self.key)
        else:
            self.key = -abs(self.key)
        geheimtext = ""
        for index, item in enumerate(self.msg):
            pos = self.alphabet.find(item)
            new_pos = (pos + self.key) % len(self.alphabet)
            geheimtext = geheimtext + self.alphabet[new_pos]
            self.log.debug(f"New Encrypted Text")
        return geheimtext.upper()

    def decrypt(self):
        return self.encrypt(key=-1)
