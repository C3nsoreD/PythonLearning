"""
The program checks if  str: s1 is an anagram of str: s2
"""
def anagram(s1, s2):
    # Remove spaces and Uppercase letter 
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    # Return boolean for the sorted match
    return sorted(s1) == sorted(s2)


def anagramTwo(s1, s2):
    # Checks
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    # check lengths 
    if len(s1) != len(s2):
        return False
        
    # hash table 
    count = {}
    for letter in s1:
        # count the number of letters
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Update the frequency table reducing the count of the elements
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        # Check if there's an extra letter
        if count[k] != 0:
            return False 

    return True

