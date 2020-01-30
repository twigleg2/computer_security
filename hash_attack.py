import hashlib
import sys
import random
import string


def SHA1_wrapper(input, n): #input string, number of bits
    mask = (2**n)-1 #produces a number whose binary representation holds a '1' in the lower n bits

    hashObject = hashlib.sha1(input.encode('utf-8'))
    digest = hashObject.digest()
    digest_int = int.from_bytes(digest, sys.byteorder)
    masked_digest = digest_int & mask
    return hex(masked_digest)

def generateRandomInput():
    alphanumeric = string.ascii_letters + string.digits
    randomString =  ''.join(random.choice(alphanumeric) for i in range(15))
    return randomString

def collisionAttack(size):
    message = generateRandomInput()
    hashes = set()
    duplicate = False
    while not duplicate:
        message += "?"
        digest = SHA1_wrapper(message, size)
        if digest in hashes:
            duplicate = True
        else:
            hashes.add(digest)

    return len(hashes)


def preimageAttack(size):
    message = generateRandomInput()
    targetDigest = SHA1_wrapper(message, size)
    digest = ""
    counter = 0
    while digest != targetDigest:
        counter += 1
        message += "?"
        digest = SHA1_wrapper(message, size)

    return counter


def main():
    sampleSize = 50
    bitSizes = [8,10,16,18]
    collisionResults = {bitSizes[0]:0, bitSizes[1]:0, bitSizes[2]:0, bitSizes[3]:0} # can I use some form of loop to do this?
    preimageResults = {bitSizes[0]:0, bitSizes[1]:0, bitSizes[2]:0, bitSizes[3]:0}

    for size in bitSizes:
        print("attacking with mask size:", end=" ")
        print(size)
        for attempt in range(sampleSize): #collision attack trials
            print("collision test number:", end=" ")
            print(attempt)
            collisionResults[size] += collisionAttack(size)
            #do 50 attacks, save the results, do some statical analysis
        for attempt in range(sampleSize): #preimage attack trials
            print("preimage test number:", end=" ")
            print(attempt)
            preimageResults[size] += preimageAttack(size)

    for size in bitSizes:
        collisionResults[size] /= sampleSize
        preimageResults[size] /= sampleSize

    print("collisionResults: ")
    print(collisionResults)
    print("preimageResults: ")
    print(preimageResults)


main()
# print(generateRandomInput())
