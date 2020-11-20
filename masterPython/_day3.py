x = [1, 3, 2, 5, 4, 9, 6]
_y = range(len(x))
y = list(range(len(x)))

def sort_x(l):
    n = len(l)
    for i in range(n - 1):
        if l[i] > l[i+ 1]:
            break
    else:
        # print('it broke')
        return

print(type(_y))  # class range
print(type(y))  # class list
print(type(sort_x))  # class function

class NewFunc(function):
    def __init__(self):
        