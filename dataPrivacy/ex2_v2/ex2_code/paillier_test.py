"""
"""
import random, sys 

from gmpy2 import mpz,f_div, powmod, invert, is_prime, random_state, mpz_urandomb, rint_round, log2, gcd 

rand=random_state(random.randrange(sys.maxsize))

# self.l is lambda and self.m is mu
class PrivateKey(object):
    def __init__(self, p, q, n):
        if p==q:
            self.l = p * (p-1)
        else:
            self.l = (p-1) * (q-1)
        try:
            self.m = invert(self.l, n)
        except ZeroDivisionError as e:
            print(e)
            exit()

class PublicKey(object):
    def __init__(self, n):
        self.n = n
        self.n_sq = n * n
        self.g = n + 1
        self.bits=mpz(rint_round(log2(self.n)))

def generate_prime(bits):    
    """Will generate an integer of b bits that is prime using the gmpy2 library  """    
    while True:
        possible =  mpz(2)**(bits-1) + mpz_urandomb(rand, bits-1 )
        if is_prime(possible):
            return possible

def generate_keypair(bits):
    """ Will generate a pair of paillier keys bits>5"""
    p = generate_prime(bits // 2)
    #print(p)
    q = generate_prime(bits // 2)
    #print(q)
    n = p * q
    return PrivateKey(p, q, n), PublicKey(n)

def enc(pub, plain):#(public key, plaintext) #to do
    # use public key
    # choose r such that gcd(r,n) = 1
    # cipher = (pub.g**message * r**pub.n )mod pub.n**2

    # Step1 choose r
    r = mpz(random.randint(1,pub.n-1))
    while not gcd(r,pub.n) == 1:
        r = mpz(random.randint(1,pub.n-1))

    # Step2 calculate cipher
    # cipher = (pub.g**plain * r**pub.n ) % pub.n**2
    # to make use of gmpy2.powmod , we do some transformation
    # use modulo ditribution: cipher :
    cipher = powmod(powmod(pub.g,plain,pub.n_sq)*powmod(r,pub.n,pub.n_sq),1,pub.n_sq)

    return cipher

def dec(priv, pub, cipher): #(private key, public key, cipher) #to do
    x = powmod(cipher,priv.l,pub.n_sq)
    L = f_div(x -1 ,pub.n)
    plain = mpz(L * priv.m) % pub.n
    return plain

def enc_add(pub, m1, m2): #to do
    """Add one encrypted integer to another"""
    return m1*m2 % pub.n_sq

def enc_add_const(pub, m, c): #to do
    """Add constant n to an encrypted integer"""
    return ((m % pub.n_sq) * powmod(pub.g,c,pub.n_sq)) % pub.n_sq

def enc_mul_const(pub, m, c): #to do
    """Multiplies an encrypted integer by a constant"""
    return powmod(m,c,pub.n_sq)


def test_data_gen(bits):
    # power(2,bits-1) to power(2,bits)
    return random.randint(2**(bits-1),2**bits)

def test(opera,bits,pub,priv):
    operand1 = test_data_gen(bits)
    operand2 = test_data_gen(bits)
    cipher1 = enc(pub,operand1)
    cipher2 = enc(pub,operand2)
    # print("operand1:", operand1,dec(priv,pub,cipher1))
    # print("operand2:",operand2,dec(priv,pub,cipher2))
    if opera == 'add_const':
        origin = operand1 + operand2
        result_cipher = enc_add_const(pub,cipher1,operand2)
    elif opera == 'add':
        origin = operand1 + operand2
        result_cipher = enc_add(pub,cipher1,cipher2)
    else:
        origin = operand1 * operand2
        result_cipher = enc_mul_const(pub,cipher1,operand2)
        
    decryp_result = dec(priv,pub,result_cipher)
    if decryp_result == origin:
        print(f"pass : {opera} on bit:{bits}")
        return True
    else:
        print(decryp_result)
        print(f"fail : {opera} on bit:{bits}")
        return False


if __name__ == '__main__':
    priv, pub = generate_keypair(1024)
    """
    test
    """
    test_result = True
    opera_list = ["add","add_const","multi"]
    for bit in range(10,500,10):
        for iter,op in enumerate(opera_list):
            test_result = test_result and test(op,bit,pub,priv)
    if test_result:
        print("all test passed")





        



