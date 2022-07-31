from __future__ import print_function

import timeit


start = timeit.default_timer()

#P = int(input(' Please enter the value of P.'))
P = 23
print('  Thanks for entering the value of P as ' + str(P))
#g = int(input(' Please enter the value of g.'))
g = 9
print('  Thanks for entering the value of g as ' + str(g))
 
#a = int(input(' \n Please enter the value of a.'))
a = 4
#b = int(input(' Please enter the value of b.'))
b = 3

# A1 Sends B2 A = g^a mod P
A = (g**a) % P
print( "\n  A1 sends over to B2: " , A )
 
# B2 Sends A1 B = g^b mod P
B = (g ** b) % P
print( "  B2 sends over to A1: " , B )

# A1 computes the Shared Secret: S_A1 = B^a mod P
A1SharedSecret = (B ** a) % P
print( "    \n  A1 Shared Secret: ", A1SharedSecret )
 
# B2 computes the Shared Secret: S_B2 = A^b mod P
B2SharedSecret = (A**b) % P
print( "  B2 Shared Secret: ", B2SharedSecret )

def generateKey(string, key): 
	key = list(key) 
	if len(string) == len(key): 
		return(key) 
	else: 
		for i in range(len(string) -
					len(key)): 
			key.append(key[i % len(key)]) 
	return("" . join(key))

print('\n')
stop=timeit.default_timer()   
print("Run time:",stop-start)
