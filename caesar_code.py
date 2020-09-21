import logging


class caesar_code:
    def __init__(self, msg: str, key: int, alphabet: str):
        """Caesar Code Object

        Args:
            msg (str): Message (Decrypted or Encrypted)
            key (int): Key to encrypt/decrypt the message
            alphabet (str): The alphabet used

        Raises:
            e: AssertionError
        """
        self.log = logging.getLogger("Caesar Verschieber")
        self.msg = msg
        self.key = key
        try:
            # Testing the arguments
            self.log.debug("Asserting correct argument types")
            assert type(msg) == str
            assert type(key) == int
            assert type(alphabet) == str

            # Alphabet String
            self.alphabet = alphabet
            self.log.debug(f"Asserting that the alphabet is 26 characters long")
            assert len(self.alphabet) == 26
        except AssertionError as e:
            # Something went wrong with the assertions
            self.log.error(f"Wrong Argument types or error with the alphabet variable")
            raise e
        else:
            self.msg = msg.lower()

    def encrypt(self, key=1):
        """Encrypts the message

        Args:
            key (int, optional): Decrypt or encrypt. Defaults to 1.

        Returns:
            str: Encrypted Message
        """
        if key == 1:
            self.key = abs(self.key)
        else:
            self.key = -abs(self.key)
        crypt = ""
        for index, item in enumerate(self.msg):
            pos = self.alphabet.find(item)
            newpos = (pos + self.key) % len(self.alphabet)
            crypt_letter = self.alphabet[newpos]
            crypt = crypt + crypt_letter
        self.log.debug(f"New Encrypted/Decrypted Text: {crypt.upper()}")
        return crypt.upper()

    def decrypt(self):
        """Decrypts the message

        Returns:
            str: Decrypted message
        """
        return self.encrypt(key=-1)
