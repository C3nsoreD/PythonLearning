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



if __name__ == "__main__":
    x = 5
    A = [6, 3, 5, 1, 6, 3, 0, 15, 12]
    B = [0, 1, 0, 0, 1, 3, 2, 2, 1, 2, 1, 3, 0, 1 ,3, 3]
    print(median(B))
    # print(count_bits(100))
    # print(parity(10001))
    # print(even_odd(A))
    print(dutch_flag_patition_1(B, 0))