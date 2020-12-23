def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A

def dutch_flag_patition(A, i):
    pivot = A[i]
    smaller = 0
    for i in range(len(A)):
        # look for small elements
        # for j in range(i + 1, len(A)):
        #     if A[j] < pivot:
        #         A[i], A[j] = A[j], A[i]
        #         break
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break 
        # for j in reversed(range(i)):
        #     if A[j] > pivot:
        #         A[i], A[j] = A[j], A[i]
        #         break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1 
    return A

def median(A):
    A = set(A)
    n = len(A)
    index = n // 2
    if n % 2:
        return sorted(A)[index]
    else:
        return sum(sorted(A)[index - 1:index+1]) /2

def dutch_flag_patition_1(A, i):
    pivot = median(A) 
    # keys = set(A)

    """
    Keep the following invariants during partitioning
    bottom group: A[:smaller]
    equal group: A[equal:equal]
    larger group: A[larger:]
    """
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    # for pivot in set(A):
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            equal, smaller = equal + 1, smaller + 1

        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
        
    return A

def plus_one(A):
    """
    Write a program which takes as input an array of digits encoding a nonnegative decimal integer
    D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
    you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
    language that has finite-precision arithmetic
    """
    # Brute force algorithim
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    
    return A

def multipy(num1, num2):
    """ Problem statement.

    """
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    
    result = [0] * (len(num1)+ len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    # print(result)
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    # print(result)
    return [sign * result[0]] + result[1:]     

def can_reach_end(A):
    """ Problem statement

    """
    further_reach, last_index = 0, len(A) - 1
    i = 0
    while i <= further_reach and further_reach < last_index:
        further_reach = max(further_reach, A[i] + i)
        i += 1
    return further_reach >= last_index


def delete_duplicate(A, key):
    """ PROBLEM
    Write a program which takes as input a sorted array and updates it so that all duplicates have been
    removed and the remaining elements have been shifted left to fill the emptied indices. Return the
    number of valid elements. 
    """
    
    if not A:
        return 0

    valid_count = 1
    for i in range(1, len(A)):
        if A[valid_count - 1] != A[i]:
            A[valid_count] = A[i]
            valid_count += 1

    return valid_count, A

def delete_duplicate_v2(A, m):
    if not A or m <= 0:
        return 0
    write_index, count = 1, 1
    for i in range(1, len(A)):
        if A[write_index - 1] == A[i]:
            count += 1
        else:
            count = 1
        if A[write_index - 1] != A[i] or count <= min(2, m):
            A[write_index] = A[i]
            write_index += 1
    return write_index

if __name__ == "__main__":
    X = [5, 0, 1]
    Y = [1, 2, 3]
    A = [2, 0, 2, 0, 1, 3, 4]
    B = [1, 0, 0, 1, 3, 2, 2, 1, 2, 1, 3, 0, 1 ,3, 3]
    C = [0, 1, 1, 2, 2, 3, 4, 5, 8]
    # print(median(B))
    # print(count_bits(100))
    # print(parity(10001))
    # print(even_odd(A))
    # print(plus_one(A))
    print(multipy(X, Y))
    print(can_reach_end(A))
    # print(dutch_flag_patition_1(B, 0))
    print(delete_duplicate(C))