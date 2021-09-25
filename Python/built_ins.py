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