import timeit
start = timeit.default_timer()

mod = 256

def KSA(key):
  key_length = len(key)
  S = list(range(mod))  # [0,1,2, ... , 255]
  j = 0
  for i in range(mod):
    j = (j + S[i] + key[i % key_length]) % mod
    S[i], S[j] = S[j], S[i]  
  
  return S


def PRGA(S):
  i = j = 0
  while True:
    i = (i + 1) % mod
    j = (j + S[i]) % mod
    S[i], S[j] = S[j], S[i]  
    K = S[(S[i] + S[j]) % mod]
    yield K


def RC4(key):
  S = KSA(key)
  return PRGA(S)

def encrypt_logic(key, text):
  key = [ord(c) for c in key]
  keystream = RC4(key)

  res = []
  for c in text:
    val = ("%02X" % (c ^ next(keystream)))  
    res.append(val)
  return ''.join(res)


def encrypt(key, plaintext):
  plaintext = [ord(c) for c in plaintext]
  return encrypt_logic(key, plaintext)


def decrypt(key, ciphertext):
  import codecs
  ciphertext = codecs.decode(ciphertext, 'hex_codec')
  res = encrypt_logic(key, ciphertext)
  return codecs.decode(res, 'hex_codec').decode('utf-8')

if __name__=="__main__":
  key = 'DAA212'
  plain_text = 'Design and Analysis of Algorithms'

  cipher_text = encrypt(key, plain_text)
  print('Encryption')
  print('plain text :', plain_text)
  print('cipher text:', cipher_text)

  decrypted = decrypt(key, cipher_text)
  print("\nDecryption")
  print('Cipher text:', cipher_text)
  print('Plain text :', decrypted)

    
print('\n')
stop=timeit.default_timer()   
print("Run time:",stop-start)