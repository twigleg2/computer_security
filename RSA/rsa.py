#gfinch

from Crypto.Util.number import getPrime

NUM_BITS = 512

def highBitSet(num, bits):
    num = num >> bits-1
    return True if num == 1 else False

def gcd(a,b): # euclids
    if b == 0:
        return a
    return gcd(b, a % b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

e = 65537
d = None
p = None
q = None
phin = None
n = None
while True:
    # ensure that the high-order bit is set in both p and q
    while True:
        p = getPrime(NUM_BITS)
        if highBitSet(p, NUM_BITS):
            break
    while True:
        q = getPrime(NUM_BITS)
        if highBitSet(q, NUM_BITS):
            break
    # ensure that (p-1)*(q-1) is relatively prime to 65537 (euclids).
    phin = (p-1)*(q-1)
    if gcd(phin, e) == 1:
        break

n = p*q
d = modinv(e, phin)

# m = # message

print("d", d)
print("p", p)
print("q", q)
print("n", n)
