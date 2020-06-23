
def multi(limit, n1, n2):
    multi1 = []
    multi2 = []
    temp = 1
    while True:
        res = n1 * temp
        if res < limit:
            multi1.append(res)
            temp += 1
        else:
            temp = 1
            break
    while True:
        res = n2 * temp
        if res < limit:
            multi2.append(res)
            temp += 1
        else:
            temp = 1
            break

    collection = list(set(multi1 + multi2))
    return (sum(collection))

print(multi(10000, 4,5))