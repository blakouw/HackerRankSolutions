def flippingBits(n):
    bin(n)
    n = ~n & 0xffffffff
    return n