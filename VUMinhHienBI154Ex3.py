import math

''' 
keypair (N,e); d
// n= (p-1)(q-1)
// d= e^-1(mod n)
// Encryption : C = M^e mod n
// Decryption : M=c^d mod n
'''


def ersa(q, p, m, e):
    return q * p, pow(e, -1, (p - 1) * (q - 1)), pow(m, e, q * p),


def drsa(q, p, c, d):
    return pow(c, d, q * p)


# q ,p ,e ,M = list(map(int ,input("input q,p,e,M \n ").split()))
# phi = ( q -1 ) * ( p -1 )
print("test encryption: p = 5, q = 11, e = 3, M = 9")
C = ersa(5, 11, 3, 9)
print(f" your key pair is: (N,e)= {C[0]}, d= {C[1]}, ciphertext is: C={C[2]}")
print("test decryption: p = 3, q = 11, d = 7, E = 5")
D = drsa(3, 11, 7, 5)
print(f"plaintext is:M={D} \n")

while True:
    print("chose 1 to encrypt, 2 to decrypt \n")
    option = int(input())
    if option == 1:
        q, p, e, M = list(map(int, input("input all your q,p,e,M \n ").split()))
        C1 = ersa(q, p, e, M)
        print(f" your key pair is: (N,e)= {C1[0]}, d= {C1[1]}, ciphertext is: C={C1[2]}")
    if option == 2:
        q, p, e, M = list(map(int, input("input all your q,p,e,C \n ").split()))
        D1 = drsa(3, 11, 7, 5)
        print(f"plaintext is:M={D1} \n")
