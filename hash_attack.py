import hashlib
import sys


def SHA1_wrapper(input, n): #input string, number of bits
    mask = (2**n)-1 #produces a number whose binary representation holds a '1' in the lower n bits

    hashObject = hashlib.sha1(input.encode('utf-8'))
    digest = hashObject.digest()
    digest_int = int.from_bytes(digest, sys.byteorder)
    masked_digest = digest_int & mask
    print(hex(masked_digest))   

def generateRandomInput():
    return "TODO"

def collisionAttack():
    pass

def preimageAttack():
    pass

def main():
    bitSizes = [8,16,20,24]

    randomInput = generateRandomInput()
    for attempt in range(50):
        randomInput += "?"
        
        

main()