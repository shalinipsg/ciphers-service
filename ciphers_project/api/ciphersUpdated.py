def caesar_cipher(plain_text, shift):
    cipher_text = ''
    for x in plain_text:
        if x.isalpha():  
            if x.islower():
                c = chr((ord(x) - 97 + shift) % 26 + 97)  
            else:
                c = chr((ord(x) - 65 + shift) % 26 + 65)  
        else:
            c = x  
        cipher_text += c
    return cipher_text
