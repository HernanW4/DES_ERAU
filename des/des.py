# The actual algorithm, encryption, decryption and what not.
from .utils import hex_to_bin
from key import Key

def greeting():
    print("Hello World")


def testing_hex_to_bin():
    value = "F"
    print(hex_to_bin(value))
