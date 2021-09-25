# zipped

x,y = map(int, input().split())

L = [map(float, input().split()) for i in range(y)]
[print(sum(i)/y) for i in zip(*L)]

# input()
x,k=map(int, input().split())
print (k==eval(input()))

# eval
eval(input())