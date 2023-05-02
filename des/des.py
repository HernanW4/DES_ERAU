# The actual algorithm, encryption, decryption and what not
from utils import *
from key import Key

def bit_xor(a,b):
    result = ""
    for i in range(len(a)):
        if a[i]==b[i]:
            result += "0"
        else:
            result += "1"
    return result

#rearrangement of plaintext bits according to a given permutation table.
def applyPerm(table, text, n):
    perm_text = ""

    for index in range(0, n):
        perm_text += text[table[index]-1]
    return perm_text

def encrypt():
     userInput = '0123456789ABCDEF'

     plaintext = hex_to_bin(userInput)
     print(plaintext)


     perm_plaintext = applyPerm(initial_perm_table, plaintext, 64)
     
     print(perm_plaintext)


encrypt()
