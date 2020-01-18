# Gaven Finch
# HW2

# ^ is XOR

bits = { # bit masks to be used later
    0: 0x1,
    1: 0x2,
    2: 0x4,
    3: 0x8,
    4: 0x10,
    5: 0x20,
    6: 0x40,
    7: 0x80,
}

# accessing the 2D array isn't quite right...
# def mixcolumns(state): #state is a 4x4  matrix
#     for y in range(4):
#         state(0, y) = ffm(0x02, state(0, y)) ^ ffm(0x03, state(1, y)) ^ state(2, y) ^ state(3, y)
#         state(1, y) = state(0, y) ^ ffm(0x02, state(1, y)) ^ ffm(0x03, state(2, y)) ^ state(3, y)
#         state(2, y) = state(0, y) ^ state(1, y) ^ ffm(0x02, state(2, y)) ^ ffm(0x03, state(3, y))
#         state(3, y) = ffm(0x03, state(0, y)) ^ state(1, y) ^ state(2, y) ^ ffm(0x02, state(3, y))


def ffm(byte1, byte2): # finite field multiply
    xtime_values = {
        0: byte1
    }

    for x in range(1,8):
        xtime_values[x] = xtime(xtime_values[x-1])

    result = 0
    for bit in bits:
        if byte2 & bits[bit]: #if bit is set
            result = result ^ xtime_values[bit]

    return result


def xtime(byte):
    byte = byte << 1
    if (byte > 0xff):
        byte = byte ^ 0x11b
    return byte


print(hex(ffm(0x22, 0x0e)))
