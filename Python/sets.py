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

# 
