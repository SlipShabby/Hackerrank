

# if-else 
n = int(input().strip())
print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")

# list comprehensions
x, y, z, n = (int(input()) for _ in range(4))
print([[a,b,c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0,z+1) if a+b+c != n])