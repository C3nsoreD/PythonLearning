"""
Given a string containing a record of the path travelled when hiking.
Check how many valleys the path contains
"""
def countingValleys(n, s):
    # 
    valley = 0
    track = 0

    for i in s:
        if i == 'U':
            track += 1
        if i == 'D':
            track -= 1
        if track == 0 and i == 'U':
            valley += 1
            
    print(valley)

s = 'UDDDUDUU'
n = len(s)
countingValleys(n ,s)