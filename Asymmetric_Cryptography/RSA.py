import timeit
start = timeit.default_timer()


import random
max_PrimLength = 1000000000000


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



def generate_keyPairs():
    p = 23
    q = 9
    
    n = p*q
    print("n ",n)
    #phi(n) = phi(p)*phi(q)
    phi = (p-1) * (q-1) 
    print("phi ",phi)
      
    e = 1
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
        
    print("e=",e," ","phi=",phi)
    d = egcd(e, phi)[1]
    
    d = d % phi
    if(d < 0):
        d += phi
        
    return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

if __name__ == '__main__':
    public_key,private_key = generate_keyPairs() 
    print("Public: ",public_key)
    print("Private: ",private_key)
    
    ctext = encrypt("Design and analysis of algorithms",public_key)
    print("encrypted  =",ctext)
    plaintext = decrypt(ctext, private_key)
    print("decrypted =",plaintext)
    
print('\n')
stop=timeit.default_timer()   
print("Run time:",stop-start)
  