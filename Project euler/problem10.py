def factorail(num):
    
    fact = 1
    lst = []
    for i in range(1, num + 1):
        lst.append(i)
        fact = fact*i
    collection = sum(lst)
    return fact, collection

print( factorail(10))


        

