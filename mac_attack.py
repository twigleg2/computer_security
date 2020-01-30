# Gaven Finch
## MAC attack

import binascii

message = "No one has completed lab 2 so give them all a 0"

messageHex = [
    0x4e, 0x6f, 0x20, 0x6f, 0x6e, 0x65, 0x20, 0x68, 0x61, 0x73, 0x20, 0x63, 0x6f, 0x6d, 0x70, 0x6c,
    0x65, 0x74, 0x65, 0x64, 0x20, 0x6c, 0x61, 0x62, 0x20, 0x32, 0x20, 0x73, 0x6f, 0x20, 0x67, 0x69,
    0x76, 0x65, 0x20, 0x74, 0x68, 0x65, 0x6d, 0x20, 0x61, 0x6c, 0x6c, 0x20, 0x61, 0x20, 0x30
]
# 17 bytes of padding needed to make 64 bytes (512 bits)
padding = 0x8000000000000000000000000000000000
mesage size = 0x00000000000001F8 #actuall message size plus key

d4 = 0x3875cb85
d3 = 0x1ed7e35a
d2 = 0x916ee4a9
d1 = 0x685117c3
d0 = 0x8129eda0


# Not my implementation of sha1
# https://codereview.stackexchange.com/questions/37648/python-implementation-of-sha1
def sha1(data, d4, d3, d2, d1, d0):
    bytes = ""

    h0 = d0
    h1 = d1
    h2 = d2
    h3 = d3
    h4 = d4

    # h0 = 0x67452301
    # h1 = 0xEFCDAB89
    # h2 = 0x98BADCFE
    # h3 = 0x10325476
    # h4 = 0xC3D2E1F0

    for n in range(len(data)):
        bytes+='{0:08b}'.format(ord(data[n]))
    bits = bytes+"1"
    pBits = bits
    #pad until length equals 448 mod 512
    while len(pBits)%512 != 448:
        pBits+="0"
    #append the original length
    pBits+='{0:064b}'.format(len(bits)-1)

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    for c in chunks(pBits, 512): 
        words = chunks(c, 32)
        w = [0]*80
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)  

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #Main loop
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = rol(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)


myMessage = ", except Gaven."
print("the new digest: ")
print(sha1(message + myMessage, d4, d3, d2,d1, d0))

print("my message in Hex:")
myMessageInHex = binascii.hexlify(b'No one has completed lab 2 so give them all a 0, except Gaven.' )
print(myMessageInHex)