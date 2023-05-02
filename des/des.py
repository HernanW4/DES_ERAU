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

def permute(before,ref,size):
    result = ""
    for i in range(0,size):
        result += before[ref[i]-1]
    return 
    
a = "1001"
b = "0110"

xorans = bit_xor(a,b)
print(xorans)