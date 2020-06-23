def intReverse(x):
    """
    Reverses a positve integer
    """
    r = 0
    while x > 0:
        r *= 10
        r += x % 10
        x //= 10
    return r

def intReverseTwo(x):
    """
    Reverses an integer of any sign
    """
    # check if x is 32 bit
    if x >= 2**31-1 or x <= -2**31: 
        return 0
    else:
        strg = str(x)
        if x >= 0:
            revst = strg[::-1]
        else:
            temp = strg[1:] 
            temp2 = temp[::-1] 
            revst = "-" + temp2
        if int(revst) >= 2**31-1 or int(revst) <= -2**31: 
            return 0
        else:
            return int(revst)

print(intReverse(123))
    