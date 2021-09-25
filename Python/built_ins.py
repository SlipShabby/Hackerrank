# zipped

x,y = map(int, input().split())

L = [map(float, input().split()) for i in range(y)]
[print(sum(i)/y) for i in zip(*L)]

# input()
x,k=map(int, input().split())
print (k==eval(input()))

# eval
eval(input())

# any and all
num, l = input(), input().split(' ')
print(all(int(i)>=0 for i in l) and any(i == i[::-1]for i in l))

# ginortS

s =sorted(input(),key=lambda x: (x.isdigit(),x.isdigit() and int(x)%2==0, x.isupper(), x.islower(),x))
print(*s, sep='')

# athlete sort

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())


arr.sort(key=lambda x: x[k])
[print(*i, sep=' ') for i in arr]


