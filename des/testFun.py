from utils import *

#rearrangement of plaintext bits according to a given permutation table.
def applyInitialPerm(pTable, plainText):
    perm_plaintext = ""

    for index in pTable:
        perm_plaintext += plainText[int(index)-1]
    return perm_plaintext

def encrypt():
     userInput = '0123456789ABCDEF'

     plaintext = hex_to_bin(userInput)
     print(plaintext)


     perm_plaintext = applyInitialPerm(initial_perm_table, plaintext)
     
     print(perm_plaintext)


encrypt()



