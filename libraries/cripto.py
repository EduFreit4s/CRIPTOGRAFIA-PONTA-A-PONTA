import secrets

# The bigger, the safer. However, large numbers consume brutal processing power
MAX_PRIME_BITS = 8     
MIN_PRIME_BITS = 6

# Size of each encrypted letter
CHAR_SIZE = 5

# This function generates random prime number based on secrets security library and the nbits interval 
def Random_prime():
    k = secrets.randbits(MAX_PRIME_BITS)
    if (k < (2**MIN_PRIME_BITS)) or k%2 == 0:
        return Random_prime()
    for i in range (2, k//2):
        if (k%i) == 0:
            return Random_prime()
    return k

# This function call random prime for generate two primes numbers distinct p and q
def Random_p_q():
    p = Random_prime()
    q = Random_prime()
    if (p == q):
        return Random_p_q()
    else:
        return p, q

#GDC
def MDC(a, b):
    if a == 0:
        return b
    else:
        gdc = MDC(b % a, a)
        return gdc

#This Euler's totient function find out how many numbers are co-primes of Phi(x) space 
def Phi(p, q):
    return (p - 1) * (q - 1)

#Product of two primes
def Semi_prime(p, q):
    return p*q

# e != 1, 1 < e < Phi
def E(phi):
    id = False
    i = secrets.randbelow(phi - 1)
    while (id != True):
        i+=1
        if MDC(phi, i) == 1:
            id = True 
            e_key = i
    return e_key

#Keys gen
def generator():
    p, q = Random_p_q()
    fi = Phi(p, q) 
    e = E(fi)
    n = p*q
    # This loop finds the modular inverse of 'e' that satisfies the equation d*e % Phi = 1
    d = fi//e
    key = False
    while key == False:
        d+=1
        if((d*e)%fi) == 1:
            key = True
    return e, n, d
    
#Encryptor
def lock(text, e, n):
    c = ""
    for i in text:
        x = (ord(i)**e)%n
        k = CHAR_SIZE-len(str(x))
        while k > 0:
            c+= "0"
            k-=1
        c+= str(x)    
    return c

#Decryptor
def unlock(text, d, n):
    m = ""
    u = ""
    for i in text:
        u+= i
        if(len(u) == CHAR_SIZE):
            m += chr((int(u)**d)%n)
            u = ""
    return m

################################# test ##################################

e, n, d= generator()
print("Public: ", e, n)
print("Private: ", d)

g = lock("me ajuda", e, n)
print("criptografado:", g)
print(unlock(g, d, n))
