""" Given a list of numbers find the pair that sums up to the given number"""

def pair(array, x):
    # check empty 
    if len(array) == 0:
        return 0

    # storage 
    seen = {}
    # for i in range(len(array)):
    #     for j in range(i + 1, len(array)):
    #         if array[i] + array[j] == x:
    #             seen.append((array[i], array[j]))

    # return seen
    for value in array:
        seen[value] = False
    
    for value in array:
        compliment = x - value
        
        if compliment in seen:
            seen[compliment] = True
            seen[value] = True

            print(value, compliment)
    print(seen)



def frequency(arry, x):
    freq_dict = {}
    for num in arry:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1
    
    print(f'the frequency of {x} is {freq_dict[x]}')


if __name__ == '__main__':
    pair([1, 2, 4, 8], 3)
    
# print(pair(, 12))

frequency([1,2,1,2,1,1,2, 3, 4, 1, 2], 1)