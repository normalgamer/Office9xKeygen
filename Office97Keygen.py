'''

Segment 1:
    4 digits
    Last digit must be 3rd digit + 1 or 2
    
Segment 2:
    Sum of digits must be divisible by 7
    Last digit can't be 0,8,9

'''

import random as rd


def generateKey():
    segment1 = rd.randint(0, 99)  # Part 1 of segment 1
    segment1num3 = rd.randint(0, 9)

    x = rd.randint(1, 2)
    segment1num4 = segment1num3 + x

    if x == 1:
        if segment1num4 == 10:
            segment1num4 = 0
        elif segment1num4 == 11:
            segment1num4 = 1
    elif x == 2:
        if segment1num4 == 10:
            segment1num4 = 1
        elif segment1num4 == 11:
            segment1num4 = 3

    segment1 = str(segment1).zfill(2)+str(segment1num3)+str(segment1num4)

    segment2 = rd.randint(0, 9999999)
    bannedSegment2 = [0, 8, 9]
    segment2sum = 0

    x = len(str(segment2))
    for i in str(segment2):
        segment2sum = int(segment2sum)+int(i)

    while (segment2sum % 7 != 0) | (str(segment2)[-1:] in bannedSegment2):
        segment2 = rd.randint(0, 9999999)
        segment2sum = 0
        for i in str(segment2):
            segment2sum = int(segment2sum)+int(i)

    return(str(segment1).zfill(4)+"-"+str(segment2).zfill(7))


print(generateKey())
input()
