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

def s_box_sub(xor):
    result = ""

    for j in range(0,8):

        rowNum1 = xor[j*6]
        rowNum2 = xor[j*6+5]
        s_row = binary_to_dec(int(rowNum1 + rowNum2))

        colNum1 = xor[j*6+1]
        colNum2 = xor[j*6+2]
        colNum3 = xor[j*6+3]
        colNum4 = xor[j*6+4]
        s_column = binary_to_dec(int(colNum1 + colNum2 + colNum3 + colNum4))

        s_box_value = s_box[j][s_row][s_column]
        result += dec_to_binary(s_box_value)

    return result

def encrypt():
     userInput = '0123456789ABCDEF'

     print(userInput)

     plaintext = hex_to_bin(userInput)
     print(plaintext)

     perm_plaintext = applyInitialPerm(initial_perm_table, plaintext, 64)
     
     print(perm_plaintext)


# Key permutation functions
def key_permutation(key):
    key_bin = hex_to_bin(key)
    round_key_bin = []


    permutated_key = applyInitialPerm(pc_1_table, key_bin, 56)

    left = permutated_key[0:28]
    right = permutated_key[28:56]

    for i in range(16):
    
        # Shifting thru the shift table
        left = shift(left, shift_table[i])
        right = shift(right, shift_table[i])

        merged = left + right

        #Round key
        r_key = applyInitialPerm(pc_2_table, merged, 48)

        # Debuging purposes
        #print("Round Key: ", bin_to_hex(r_key))

        round_key_bin.append(r_key)

    return round_key_bin

#key = Key()
#key.make_key()
#
#print("First Key: ", key)
#key_permutation(key.full_string())








