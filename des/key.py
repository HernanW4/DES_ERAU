import random

# Made by yours truly Walter Hernandez :)

# Because our key is going to be in Hex form this is the ALPHABET we use
ALPHABET = "0123456789ABCDEF"

# Template = "AAAA-BBBB-CCCC-DDDD"


# Class that will hold the key, to be fair I don't why I made it a class
# But who cares

class Key():
    def __init__(self):
        self.key = ''

    # This is so you can print the class using the print() method
    def __repr__(self):
        return f"Key: {self.key}"

    # Where the magic happens, it won't return the key it will just make it.
    def make_key(self):
        key = ''
        chunk = ''
        #This will run until the right randomnes
        while True:
            while len(key) < 20: #Length is 20 because of the hyphons, but it wil
                                # return a 56 bit key
                c = random.choice(ALPHABET)
                key += c
                chunk += c
                if len(chunk) == 4:
                    key += '-'
                    chunk = ''
            key = key[:-1]
            if self.verify_key(key):
                self.key = key
                break
            else:
                key = ''

    # Verification purposes of the key, DO NOT CALL IT no need to :)
    def verify_key(self, key):
        total_value = 0
        digit_count = 0
        verify_digit = key[2] # The digit we going to use for verification
        split = key.split("-")
        for chunk in split:
            if len(chunk) != 4:
                return False
            for c in chunk:
                if c == verify_digit:
                    digit_count += 1
                total_value += ord(c)

        # This is the criteria I use for verification purposes
        # It can be modified to our liking but its simple enough
        if (total_value >= 1040 and total_value <= 1100) and digit_count == 3:
            return True
        return False

    # This is to return the actual key with no hyphons
    def full_string(self):
        key = self.key.split("-")
        return "".join(key)
