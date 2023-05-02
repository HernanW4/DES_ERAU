# The actual algorithm, encryption, decryption and what not.
from utils import *
#from .key import Key


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

def encrypt(plaintext, roundkeys):
     
     userInput = '0123456789ABCDEF'

     plaintext = hex_to_bin(userInput)
     print(plaintext)


     perm_plaintext = applyPerm(initial_perm_table, plaintext, 64)
     print(perm_plaintext)

     # Splitting
     LHS = plaintext[0:32]
     RHS = plaintext[32:64]


# Key permutation functions
def key_permutation(key):
    key_bin = hex_to_bin(key)
    round_key_bin = []


    permutated_key = applyPerm(pc_1_table, key_bin, 56)

    left = permutated_key[0:28]
    right = permutated_key[28:56]

    for i in range(16):
    
        # Shifting thru the shift table
        left = shift(left, shift_table[i])
        right = shift(right, shift_table[i])

        merged = left + right

        #Round key
        r_key = applyPerm(pc_2_table, merged, 48)

        # Debuging purposes
        #print("Round Key: ", bin_to_hex(r_key))

        round_key_bin.append(r_key)

    return round_key_bin

#key = Key()
#key.make_key()
#
#print("First Key: ", key)
#key_permutation(key.full_string())








