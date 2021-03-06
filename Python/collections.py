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

# default dict

from collections import defaultdict

n,m = map(int,input().split())
d = defaultdict(list)
l =[]
l1 = []

for i in range(n):
    l.append(input())
    
for i in range(m):
    l1.append(input())

for i in range(n):
    d[l[i]].append(i+1)

for i in l1:
    if i in d:
        print(*d[i])
    else:
        print(-1)

# named tuple

from collections import namedtuple

# n = int(input())       
# s = list(map(str,input().split()))

# x = 0
# for i in range(len(s)):
#     if s[i] == 'MARKS':
#         x = i

# l = []
# for i in range(n):
#     l.append(int((input().split())[x]))
# print(sum(l)/n)


# n = int(input())
# i = input().split().index('MARKS')
# l = []

# for _ in range(n):
#     l.append(int((input().split())[i]))
# print(sum(l)/n)

n= int(input())
Students = namedtuple('student',input().split())
total = 0

for i in range(n):
    line = Students(*input().split())
    total += int(line.MARKS)
print(total/n)


# ordered dict
from collections import OrderedDict

products = OrderedDict()

for i in range(int(input())):
    p, price = input().rsplit(' ',1)
    products.setdefault(p, 0)
    products[p] += int(price)
    
[print(k,v) for k,v in products.items()]

# deque

from collections import deque

d= deque()

for i in range(int(input())):
    cmd = input().split()
    if len(cmd) == 1:
        getattr(d, cmd[0])()
    else:
        getattr(d,cmd[0])(cmd[1])
[print(x, end=' ') for x in d]

# word order

from collections import OrderedDict

d = OrderedDict()

for i in range(int(input())):
    w = input()
    d.setdefault(w, 0)
    d[w] +=1
l =[(v) for x,v in d.items()]
print(len(l))
print(*l)  

# company logo

from collections import Counter

if __name__ == '__main__':
    s = input()
    [print(a,b) for a,b in (Counter(sorted(s)).most_common(3))]


# piling up

from collections import deque

for i in range(int(input())):  
    i, queue =input(), deque(map(int, input().split()))
    # print(queue)
    for cube in reversed(sorted(queue)):
        if queue[-1] == cube: 
            queue.pop()
        elif queue[0] == cube: 
            queue.popleft()
        else:
            print('No')
            break
    else: 
        print('Yes')
