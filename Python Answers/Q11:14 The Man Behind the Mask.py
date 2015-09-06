def check_bit4(input):
#I prefer to implicitly include the mask instead of declaring a variable.
    if input & 0b1000 > 0:
        return "on"
    else:
        return "off"