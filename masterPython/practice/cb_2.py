# You want to keep a limited history of the last few items seen during iteration or during
# some other kind of processing
from collections import deque

# Generator function
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in lines:
            yield line, previous_lines
        previous_lines.append(line)

# Tests
# words =[
#     'THis is a python line one',
#     'this is not a java but python line 2',
# ]
# x = [(line, prelines) for line, prelines in search(words, 'python')]
# print(x)

def first_n(n):
    '''Build and retrurn a list'''
    num, nums = 0, []
    while num < n:
        # nums.append(num)
        yield num
        num += 1
    # return nums

## Implemeting a generator pattern (an iterable)
class First_n(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        raise StopIteration()


if __name__ == "__main__":
    with open('file.txt') as f:
        lines = f.readlines()
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline)
            print(line)
            print('-'*20)
