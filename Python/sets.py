# intro

def average(array):
    # your code goes here
    s = set(array)
    # print(s)
    return sum(s)/len(s)
    
# no idea

input()
arr = input().split()
a,b = (set(input().split()) for i in range(2))
print(sum((i in a) - (i in b) for i in arr))

# symmetric difference

a,b = [set(input().split(' ')) for i in range(4)][1::2]
# d = list(b.difference(a).union(a.difference(b)))
# x = sorted(d,key = int)
print ('\n'.join(sorted(a^b, key=int)))
# for c in x:
    # print(c)

# add

# a = set()
# for i in range(int(input())):
#     a.add((input()))
# print(len(a))

print(len({input() for i in range(int(input()))}))

# discard, remove, pop

n = int(input())
s = set(map(int, input().split()))
# print(s)

for i in range(int(input())):
    args, *kwargs = map(str,input().split())
    getattr(s,args)(*(int(x) for x in kwargs))

print (sum(s))

# union

a, b = [set(input().split()) for i in range(4)][1::2]
print(len(a.union(b)))

# intersection

a, b = list((set(input().split()) for i in range(4)))[1::2]
print(len(a.intersection(b)))

# difference

a, b = list(set(input().split()) for i in range(4))[1::2]
print(len(a.difference(b)))

# symmetric difference

a, b = list(set(input().split())for i in range(4))[1::2]
print(len(a.symmetric_difference(b)))

# mutations

int(input())
s = set(input().split())
n =int(input())

for i in range(n):
    command, *args = input().split()
    # print(command, *args)
    getattr(s, command)(set(input().split())) 
    
print(sum(map(int, s)))