def funct(q):
    moves = 0 
    Q = [P-1 for P in q]
    print(Q)

    for i, P in enumerate(Q):
        # print(i, P)
        if P - i > 2:
            print("Too chaotic")
            return

        for j in range(max(P-1, 0), i):
            # print(Q[j], P)
            print(P, range(max(P-1, 0), i))
            if Q[j] > P:
                moves += 1
    print("moves: ",moves)


def minimumBribes(q):
    # create a ordered list of length = len(q)
    # iterate over the q and compare positions with the ordered list 
    ordered = sorted(q)
    result = 0
    # print(ordered)
    for i in range(len(q)):
        # compare the elements
        if ordered[i] == q[i]:
            continue
        
        q_index = q.index(ordered[i])

        print(q_index, q[i], ordered.index(ordered[i]), ordered[i])
        if abs(ordered.index(ordered[i]) - q_index) <= 2:
            diff = abs(ordered.index(ordered[i]) - q_index)
            # print(diff)
            result += diff

        else:
            # [1, 2, 3, 4]      [1, 4, 2, 3]
            # print(ordered.index(ordered[i]), q[i])
            # diff = abs(ordered.index(ordered[i]) - q_index)
            # print(diff)
            # result += diff
            print('Too chaotic')
            return

        
    # for i, P in original_q:
    #     if abs(original_q.index(original_q[i]) - q_index) > 2:

    print(result//2)

# q = [5, 1, 2, 3, 7, 8, 6, 4]
q = [1, 2, 5, 3, 7, 8, 6, 4]
print(funct(q))