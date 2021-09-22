# Counter

from collections import Counter

x = int(input())
shoes = Counter(map(int, input().split()))

total = 0

for i in range(int(input())):
    size, price = map(int, input().split())
    if shoes[size]:
        total += price
        shoes[size] -=1

print(total)

