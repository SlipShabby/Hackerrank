import cmath

# polar coord

z = cmath.polar(complex(input()))
print(z[0], z[1], sep = '\n')

# angle mbc
ab, bc = [float(input()) for i in range(2)]

ac = math.hypot(ab,bc)
d ='\u00b0'

print(round(math.degrees(math.acos(bc/math.hypot(ab,bc)))),d, sep = '')

# triangle quest 

for i in range(1,int(input())):
    print((10**(i)//9)*i)

# triangle quest 2

set(map(lambda x:print((10**x//9)**2),range(1,int(input())+1)))

# mod divmode

a, b = [int(input()) for i in range(2)]
print(a//b, a%b, a.__divmod__(b), sep='\n')

# mod power

a,b,c = [int(input()) for i in range(3)]
print(pow(a,b), pow(a,b,c), sep = '\n')

# integers come in all size

a,b,c,d = [int(input()) for i in range(4)]
print(pow(a,b) + pow(c,d))