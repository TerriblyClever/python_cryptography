#Transposition Cipher
import math
import detectEnglish

def transposition_encrypt(key, plain_text):
    #create a list to hold the ciphertext
    ciphertext_list = [""]*key
    
    for column in range(key): #loop (key) number of times, once
        index = column #once for each "column", or string in list
                
        #will run as long as length of message is not exceeded
        while index < len(plain_text):
            ciphertext_list[column] += plain_text[index]
            index += key #moving (key) number of characters
                         #down the plain_text string
                         
    return ("".join(ciphertext_list))
       
def transposition_decrypt(key, cipher_text):
    
    #converts value to next highest integer
    columns = math.ceil(len(cipher_text)/key)
    rows = key
    empty = (columns * rows)-len(cipher_text)
    
    plain_text = ['']*columns
    index = 0 #start decryption in column zero
    row = 0
    
    for letter in cipher_text: #loops through each letter
        plain_text[index] += letter #of the message
        index += 1 #shift over one column
        
        #reset in last column
        if index == columns:
            index = 0 #moved back to first column
            row += 1 #moved down a row
        
        #reset in the next to last column        
        elif index == columns - 1 and row >= rows - empty:
            index = 0 #moved back to first column
            row += 1 #moved down a row

    return ''.join(plain_text)      
    
    
def transposition_hack(cipher_text):
    for key in range(1, len(cipher_text)):
        print("Trying key #{}...".format(key))
        
        decrypted_text = transposition_decrypt(key, cipher_text)
        
        if detectEnglish.isEnglish(decrypted_text):
            print("\nPossible encryption hack:")
            print("Key {}:{}".format(key, decrypted_text[:200]))
            print("\nEnter D if done, anything else to continue hacking:")
            response = input(">> ")
            
            if response.strip().upper().startswith("D"):
                return decrypted_text
    
    return None
    
    
    
  
    
      
          