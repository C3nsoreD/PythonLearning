'''
Given an integer array, output all the unique pairs that sum up
to a specific value k.

'''

def pair_sum(array, x):
    # if the array is too small
    if len(array) < 2:
        return 0
    
    # Unique storage
    seen = set()
    output = set()

    for num in array:
        val = x - num 
        if val not in seen:
            seen.add(num) # collects all unique 
        else:
            # output.add((num, target))
            output.add((min(num, val), max(num, val)))
 
    print('\n'.join(map(str, list(output))))

pair_sum([1, -1, 5, 5, 7], 6)