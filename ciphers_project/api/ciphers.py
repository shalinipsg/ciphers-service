def ciphers_fun(plain_text, shift):
    cipher_text=''
    for x in plain_text:
        c=ord(x)+shift
        c=chr(c)
        cipher_text+=c
    return cipher_text