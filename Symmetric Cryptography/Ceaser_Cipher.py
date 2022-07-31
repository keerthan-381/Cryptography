import timeit
start = timeit.default_timer()


def main():
    plaintext = 'Design and Analysis of Algorithms'
    key = 19
    print()
    ciphertext = caesarEncryption(plaintext, key)
    plaintext = caesarDecryption(ciphertext, key)
    print()
    print("Encrypted ciphertext is : ", ciphertext)
    print("Decrypted plaintext is  : ", plaintext)
    print()
    return

def caesarEncryption(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        ascii = ord(letter)
        if letter.isalpha():
            temp = ascii + key
            if (temp > 90 and letter.isupper()) or (temp > 122 and letter.islower()):
                ciphertext += chr(temp - 26)
            else:
                ciphertext += chr(temp)
    return ciphertext

def caesarDecryption(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        ascii = ord(letter)
        if letter.isalpha():
            temp = ascii - key
            if ( (temp < 65 and letter.isupper()) or (temp < 97 and letter.islower()) ):
                plaintext += chr(temp + 26)
            else:
                plaintext += chr(temp)
    return plaintext

if __name__ == "__main__":
    main()
    
print('\n')
stop=timeit.default_timer()   
print("Run time:",stop-start)