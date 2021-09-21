import cmath

# polar coord

z = cmath.polar(complex(input()))
print(z[0], z[1], sep = '\n')

# angle mbc
ab, bc = [float(input()) for i in range(2)]

ac = math.hypot(ab,bc)
d ='\u00b0'

print(round(math.degrees(math.acos(bc/math.hypot(ab,bc)))),d, sep = '')

