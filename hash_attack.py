import hashlib

def SHA1_wrapper(str, n): #input string, number of bits
    pass

testString = "This is a test"
digest = hashlib.sha1(testString.encode('utf-8')).hexdigest()
digest = bytearray(digest)
print(digest[-8:])
