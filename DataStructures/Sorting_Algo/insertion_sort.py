# Quick demo of insertion sort algorthim

def insertionsort(lst):
    for index in range(1 ,len(lst)):
        curr = lst[index]
        pos = index
        print(pos)
        while pos > 0 and lst[pos-1] > curr:
            lst[pos] = lst[pos-1]
            pos = pos - 1
        lst[pos] = curr

lst = [2,8,5,7,1,6,0]
insertionsort(lst)
print(lst)
