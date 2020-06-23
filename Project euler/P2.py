'''
Prolem 2 in the project euler problems
'''
def fib():
    a, b = 0, 1
    check = True
    fibLst = []
    while check:
        c = a + b
        a = b
        b = c
        #print b
        fibLst.append(b)
        if b >= 3000000:
            check = False
    return fibLst


def main():
    fLst = fib()
    # fib number holder
    fbHld = []
    for i in fLst:
        if i % 2 == 0:
            fbHld.append(i)
            
    print(sum(fbHld))

main()


