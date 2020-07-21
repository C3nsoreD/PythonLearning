"""
Complete the function minimumBribes in the editor below. 
It must print an integer representing the minimum number of bribes necessary, 
    or Too chaotic if the line configuration is not possible.

Print an integer denoting the minimum number of bribes needed to get the queue into its final state. 
Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.
"""

def minimum_bride(q):
    moves = 0
    Q = [P-1 for P in q]
    for i, P in enumerate(Q):

        if P - i > 2:
            print('too chaotic')
            return
        for j in range(max(P-1,0), i):
            print(f'j:{j}, i:{i}, q[j]:{Q[j]}, p:{P}. ')    
            if Q[j] > P:
                print(f'q[j]:{Q[j]}, p:{P}')
                moves += 1
    
    return moves

q = [2, 4, 1, 3, 5]
minimum_bride(q)