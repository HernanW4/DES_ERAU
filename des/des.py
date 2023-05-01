# The actual algorithm, encryption, decryption and what not.
from .utils import hex_to_bin
from .key import Key

def bit_xor(a,b):
    result = ""
    for i in range(len(a)):
        if a[i]==b[i]:
            result += "0"
        else:
            result += "1"
    return result