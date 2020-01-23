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
    randomInput = generateRandomInput()
    hashes = {}

def preimageAttack():
    randomInput = generateRandomInput()
    hashes = {}

def main():
    sampleSize = 50
    bitSizes = [8,16,20,24]
    collisionResults = {bitSizes[0]:0, bitSizes[1]:0, bitSizes[2]:0, bitSizes[3]:0}
    preimageResults = {bitSizes[0]:0, bitSizes[1]:0, bitSizes[2]:0, bitSizes[3]:0}

    for size in bitSizes:
        for attempt in range(sampleSize): #collision attack trials
            collisionResults[bitSizes[size]] += collisionAttack(size)
            #do 50 attacks, save the results, do some statical analysis
        for attempt in range(sampleSize): #preimage attack trials
            preimageResults[bitSizes[size]] += preimageAttack(size)
    
    for size in bitSizes:
        collisionResults[size] /= sampleSize
        preimageResults[size] /= sampleSize
        

myset = {1,2,3,4,5,6,7,8,9}
print(myset)
print(1 in myset)
print(0 in myset)
myset.add(0)
myset.add(1)
print(myset)
print(1 in myset)
print(0 in myset)

# main()