# Selection sort implentaion

def selectionsort(lst):
    for i in range(0, len(lst)):
        min = i 
        for j in range(i, len(lst)):
            if lst[j] < lst[min]:
                min = j
        temp = lst[i]
        lst[i] = lst[min]
        lst[min] = temp

lst = [2,1,0,4,9]
selectionsort(lst)
print(lst)
