# We will use this python file to test out our stuff
# Annoying? I don't care

import sys
import os

from des import des
from des import utils
from des.key import Key

from pick import pick

#Main function
def main():
    my_key = Key()
    my_key.make_key()
    roundkeys = des.key_permutation(my_key.full_string())
    while True:
        title = 'Choose an option below'
        options = ['Encryption', 'Decryption', 'Display key generation', "Exit"]

        option, index = pick(options, title, indicator='=>', default_index=2)

        print(f"You chose {option} at index {index}")
        os.system("cls")
        os.system("clear")
        if index == 0:
            plaintext = input("Input message to encrypt: ")
            
        

           # print("First Key: ", key)
        

            plaintext = '123456ABCD132536'

            ciphertext = des.encrypt(plaintext,roundkeys)
            #des.encrypt(plaintext, roundkeys)
            print("cipher Text : ", utils.bin_to_hex(ciphertext))
            input("press enter to continue...")

            
        if index == 1:
            if len(plaintext) == 0:
                print("please go back and encrypt a message first")
                print("press enter to continue")
                input("press enter to continue...")
            else:
                
                ciphertext = input("Input message to decryptt: ")
                roundkeys_rev = roundkeys[::-1]
                

                plaintext = utils.bin_to_hex(des.encrypt(ciphertext, roundkeys_rev))
                print("Plain Text : ", plaintext)
                input("press enter to continue...")

        if index == 2:
            key = Key()
            newkey = key.make_key()
            print("This is your new key: ", key)
            input("press enter to continue...")

        if index == 3:
            break


#run main fucntion
if __name__ == '__main__':
    
    main()
   


# This is window stuff :)
#app = QApplication(sys.argv)
#
#window = MyWindow()
#window.update_encrypted_label("Hellocsacascascascascaschjbashgcvajshefgbakuywyehjsfgfbkarsjhfbkawhjesfbnakrjhsgbajkhrsnmgbvkjahr,smngbv kjha,nmsfbgv kjh,arsmngbv j,asnm")
#window.update_decrypted_label("Hellocsacascascascascaschjbashgcvajshefgbakuywyehjsfgfbkarsjhfbkawhjesfbnakrjhsgbajkhrsnmgbvkjahr,smngbv kjha,nmsfbgv kjh,arsmngbv j,asnm")
#window.show()
#
#sys.exit(app.exec_())





