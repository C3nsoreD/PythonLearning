def intReverse(x):
    r = 0
    while x != 0:
        r *= 10
        r += x % 10
        x //= 10
    return r

print(intReverse(-123))
