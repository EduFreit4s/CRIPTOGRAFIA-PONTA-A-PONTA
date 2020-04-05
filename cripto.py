import secrets

# The bigger, the safer. However, large numbers consume brutal processing power
MAX_PRIME_BITS = 8     
MIN_PRIME_BITS = 6

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



def MDC(a, b):
    if a == 0:
        return b
    else:
        gdc = MDC(b % a, a)
        return gdc

#This Euler's totient function find out how many numbers are co-primes of Phi(x) space 
def Phi(p, q):
    return (p - 1) * (q - 1)

def Semi_prime(p, q):
    return p*q

def E(phi):
    id = False
    i = secrets.randbelow(phi - 1)
    # e != 1, 1 < e < phi
    while (id != True):
        i+=1
        if MDC(phi, i) == 1:
            id = True 
            e_key = i
    return e_key


def generator():
    p, q = Random_p_q()
    fi = Phi(p, q) 
    e = E(fi)
    # This loop finds the modular inverse of 'e' that satisfies the equation i*e % Phi = 1
    i = 1
    key = False
    while key == False:
        i+=1
        if((i*e)%fi) == 1:
            key = True
    return e, p*q, i
    

def lock(text, e, semiprime):
    c = ""
    for i in text:
        x = (ord(i)**e)%semiprime
        c+= str('%08d'%x)
    return c

def unlock(text, y, semiprime):
    txt = ""
    u = ""
    for i in text:
        u+= i
        if(len(u) == 8):
            txt += chr((int(u)**y)%semiprime)
            u = ""
    
    return txt


