#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Dinesh
#
# Created:     06-03-2020
# Copyright:   (c) Dinesh 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
p=0
for a in range(99,10,-1):
    for b in range(99,10,-1):
        c=a*b
        if p<c:
            p=c
            while p != 0:
                r = p % 10
                rn = r * 10 + r
                rn /= 10;
                if p==rn:
                    print(p)
print(p)