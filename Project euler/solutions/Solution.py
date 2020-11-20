# Solution object
## follows a typical solution schema

class Solution:
    def __init__(self, input=None):
        self._input = input

    def result(self, func: function):
        if self._input:
            print(func(self._input))
        else:
            print(func)

# print a sum
# x = [1, 2, 4]
    
# def _sum(x: list):
#     s = 0
#     for i in x:
#         s += i
#     return s


# my_sum = Solution(x)

# my_sum.run(_sum)