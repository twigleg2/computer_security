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
        if highBitSet(p):
            break
    while True:
        q = getPrime(NUM_BITS)
        if highBitSet(q):
            break
    # ensure that (p-1)*(q-1) is relatively prime to 65537 (euclids).
    phin = (p-1)*(q-1)
    if gcd(phin, e) == 1:
        break

n = p*q
d = # calculate - d = multiplicative inverse of e mod phin (use extended euclids)

# m = # message



print("p", p)
print(gcd(35,15))