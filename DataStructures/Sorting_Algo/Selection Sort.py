# Selection sort implentaion

def selectionsort(lst):
    for i in range(0,len(lst)-1):
        min = 1
        for j in range(1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp

lst = [2,1,0,4,6,2,9]
selectionsort(lst)
print(lst)
