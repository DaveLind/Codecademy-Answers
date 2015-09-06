def flip_bit(number, n):
    mask = (0b1 << n-1)
    #remember must be n-1 as we start by flipping the first 1 bit.
    result = bin(number ^ mask)
    return result