
def countingValleys(n, s):
    valley = 0
    track = 0
    for i in s:
        if i == 'U':
            # if track == 0:
            #     valley += 1
            #     track += 1
            track += 1
        if i == 'D':
            track -= 1
            # else:
            #     track -= 1
        if track == 0 and i == 'U':
            valley += 1
        # print(valley)
    print(valley)

s = 'UDDDUDUU'
n = len(s)
countingValleys(n ,s)