
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