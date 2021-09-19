# list comprehensions
x, y, z, n = (int(input()) for _ in range(4))
print([[a,b,c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0,z+1) if a+b+c != n])


# runner score
n = int(input())
arr = map(int, input().split())
l = list(set(sorted(arr)))
print(l[-2])

# nested lists

n = int(input())
marks = [[input(), float(input())] for _ in range(n)]

scores = sorted(set(mark for name, mark in marks))[1]
print('\n'.join([a for a,b in sorted(marks) if b == scores]))

# finding the percentqage

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

print(f"{sum(student_marks[query_name])/len(student_marks[query_name]):.2f}")