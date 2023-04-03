# Nathan Fleet
# Encryption Program - Homework 5 HIC
# 4/2/2023


def encrypt(plaintext, key):
    encryptedtext = ""
    
    for c in plaintext:
        if c != ' ':
            c = chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            encryptedtext += c
        else:
            encryptedtext += ' '
    
    return encryptedtext

if __name__ == '__main__':
    fullname = "nathan fleet"
    
    print("My name (unencrypted): Nathan Fleet")
    print("I am going to use the ceaser cipher to encrypt my full name")
    
    key = int(input("Enter key for cipher: "))
    print()
    
    fullname = encrypt(fullname, key)
    
    print(f"My name (encrypted) with key {key}: {fullname}")
