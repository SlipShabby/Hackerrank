
# product()

from itertools import product

a, b =list(map(int,input().split()) for i in range(2))
print(*product(a,b), sep= ' ')
# print(list(a),list(b))


# permutations

from itertools import permutations

a,b=(input().split())
s = list(sorted(permutations(a,int(b))))
# for i in range(len(s)):
#     print(''.join(s[i]))

print(*[''.join(i) for i in s], sep = '\n')

# combinations

from itertools import combinations

a,b = input().split()
# s = list(combinations(sorted(a), int(i)))
for i in range(1,int(b)+1):
    print(*[''.join(i) for i in combinations(sorted(a), int(i))], sep= '\n')


# combinations with replacemnet

from itertools import combinations_with_replacement
a,b = input().split()

s = list(combinations_with_replacement(sorted(a), int(b)))

print(*[''.join(i) for i in (s)], sep='\n')

# compress the string

from itertools import groupby
a = [(len(list(g)), int(k)) for k, g in groupby(input())]
print(*a)

# iterables & iterators

from itertools import combinations

n = int(input())
a = input().split()
k = int(input())

c = list(combinations(a,k))
f = [i for i in c if 'a' in i]
print(len(f)/len(c))

# maximaze it

from itertools import product

k , m = map(int, input().split())
l = [(i**2 for i in list(map(int, input().split()))[1:]) for _ in range(k)]
# l2 = [sum(i)%m for i in range(list(*product))]
l2 = []
for i in list(product(*l)):
    l2.append(sum(i)%m)
print(max(l2))





