#Caesar Cipher, caesar_cipher

import detectEnglish

def caesar_encrypt(ENCRYPT_KEY, PLAIN_TEXT):
    CIPHER_TEXT = "" #initialize plain_text to empty string)
    for letter in PLAIN_TEXT:
        position = ord(letter) #set position to ASCII table position
        if position >= 65 and position <= 90:#only shift characters that are letters
            position = ord(letter) + ENCRYPT_KEY #sets to the encrypt position of the letter   
            if position > 90:
                position = position - 26
                CIPHER_TEXT += chr(position)
            else:
                CIPHER_TEXT += chr(position)
        else:
            CIPHER_TEXT += letter
    
    return CIPHER_TEXT


def caesar_decrypt(ENCRYPT_KEY, CIPHER_TEXT):
    PLAIN_TEXT = "" #initialize plain_text to empty string
    for letter in CIPHER_TEXT:
        position = ord(letter) #set position to ASCII table position
        if position >= 65 and position <= 90:#only shift characters that are letters
            position = ord(letter) - ENCRYPT_KEY #sets to the encrypt position of the letter   
            if position < 65:
                position = position + 26
                PLAIN_TEXT += chr(position)
            else:
                PLAIN_TEXT += chr(position)
        else:
            PLAIN_TEXT += letter
    
    return PLAIN_TEXT
    
    
def cc_hack(CIPHER_TEXT):
    for shift in range(1, 26):
        print("Trying key #{}...".format(shift))
        
        decrypted_text = caesar_decrypt(shift, CIPHER_TEXT)

        if detectEnglish.isEnglish(decrypted_text):
            print("Possible hack detected...")
            print("Key: {} Possible plaintext: {}".format(shift, decrypted_text[:100]))
            print("Enter D to exit the hack, any other key to continue.")
            response = input(">> ").upper().strip()
            
            if response == "D":
                return decrypted_text
                
    return None











