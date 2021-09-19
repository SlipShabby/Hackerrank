
# runner score

n = int(input())
arr = map(int, input().split())

l = list(set(sorted(arr)))

print(l[-2])