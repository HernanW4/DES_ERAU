# The actual algorithm, encryption, decryption and what not
from utils import *
from key import Key

#returns the results of two values XORed together - Olivia
def bit_xor(a,b):
    result = ""
    for i in range(len(a)):
        if a[i]==b[i]:
            result += "0"
        else:
            result += "1"
    return result


#rearrangement of plaintext bits according to a given permutation table. - Calla
def applyPerm(table, text, n):
    perm_text = ""

    for index in range(0, n):
        perm_text += text[table[index]-1]
    return perm_text

#uses the result from the XOR function to get s-box permutation result - Olivia
def s_box_sub(xor):
    result = ""

    for j in range(0,8):

        #calculates s-box row
        rowNum1 = xor[j*6]
        rowNum2 = xor[j*6+5]
        s_row = binary_to_dec(int(rowNum1 + rowNum2))
        #print(s_row)

        #calculates s-box column
        colNum1 = xor[j*6+1]
        colNum2 = xor[j*6+2]
        colNum3 = xor[j*6+3]
        colNum4 = xor[j*6+4]
        s_column = binary_to_dec(int(colNum1 + colNum2 + colNum3 + colNum4))
        #print(s_column)

        #retrieves s-box value
        s_box_value = s_box[j][s_row][s_column]
        result += dec_to_binary(s_box_value)

    return result

#takes in plaintext and roundkeys to complete DES encryption with 16 Feistal rounds - Calla/Walter/Olivia
def encrypt(plaintext,roundkeys):

    plaintext = hex_to_bin(plaintext)
    #print(plaintext)

    #initial permutation
    perm_plaintext = applyPerm(initial_perm_table, plaintext, 64)
     
    print("Perm plaintext: ",bin_to_hex(perm_plaintext))

    #splits permutated text into two halves
    LHS = perm_plaintext[0:32]
    RHS = perm_plaintext[32:64]

    print("Perm plaintext: ",bin_to_hex(LHS))
    print("Perm plaintext: ",bin_to_hex(RHS))

    #begins feistal rounds
    for i in range(0,16):

        #expansion d-box
        RHS_expanded = applyPerm(expansion_table,RHS,48)

        #XOR with first round key 
        xor_with_rk = bit_xor(RHS_expanded,roundkeys[i])

        #retrieves result from s-box function 
        s_box_result = s_box_sub(xor_with_rk)
         
        #retrieves straight permutation result 
        straight_perm_result = applyPerm(straight_perm_table,s_box_result,32)

        #XORs output from overall function with LHS 32-bits
        LHS = bit_xor(LHS,straight_perm_result)

        #prints out each round and 64-bit output
        if( i!=15):
            LHS,RHS = RHS,LHS
        print("Round",i+1,": ",bin_to_hex(LHS)," ",bin_to_hex(RHS))
    merged = LHS + RHS

    #displays final ciphertext
    ciphertext = applyPerm(final_perm,merged,64)

    return ciphertext


# Key permutation functions - Walter
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

#displays functionality of all code
key = Key()
key.make_key()

key = "AABB09182736CCDD"

print("First Key: ", key)
roundkeys = key_permutation(key)

plaintext = '123456ABCD132536'

ciphertext = encrypt(plaintext,roundkeys)

print("Ciphertext: ",bin_to_hex(ciphertext))






