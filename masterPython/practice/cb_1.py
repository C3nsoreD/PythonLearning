# clever recursive algo with unpacking 

def my_sum(ar):
    head, *tail = ar
    return head + my_sum(tail) if tail else head
lst = [1, 2, 4, 2, 5, 9, 0]

lst_2 = lst[:1]

# print(my_sum(lst))
# print(my_sum(lst_2))

# You want to keep a limited history of the last few items seen during iteration or during
# some other kind of processing
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in lines:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == "__main__":
    with open('file.txt') as f:
        for line, prevlines in search(f, 'example', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
