def main(arr):
    table = {}
    for i in range(len(arr)):
        if arr[i] not in table:
            table[arr[i]] = 1
        else:
            table[arr[i]] += 1

    print(solution2(arr, table))

def isunique(table):
    for k in table:
        if k in table:
            pass

def solution2(arr, table):
    for k in table:
        while (table[k] > 1) and isunqiue(table):
            arr.insert(arr.index(k), 2*k)
            arr.remove(k) 
            table[k] -= 1
        print(table[k], k)
    return arr

main([3, 1, 1, 2, 4, 5, 2])