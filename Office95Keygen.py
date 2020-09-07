'''

Segment 1:
    3 digits long
    
Segment 2:
    Sum of digits must be divisible by 7
    
'''

import random as rd


def generateKey():
    segment1 = rd.randint(0, 999)

    segment2sum = 0
    segment2 = rd.randint(0, 9999999)

    for i in str(segment2):
        segment2sum = int(segment2sum)+int(i)

    while (segment2sum % 7 != 0):
        segment2 = rd.randint(0, 9999999)
        segment2sum = 0
        for i in str(segment2):
            segment2sum = int(segment2sum)+int(i)

    return(str(segment1).zfill(3)+"-"+str(segment2).zfill(7))


print(generateKey())
input()
