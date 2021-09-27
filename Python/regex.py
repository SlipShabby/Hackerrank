import re


# detect float num

# for i in range(int(input())):
#     n = input()
#     if n == '0':
#         print('False')
    
#     try:
#         if float(n):
#             print('True')
#     except:        
#         print('False')


for i in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

# re.split()

regex_pattern = r"[.\,]"

# group()

s = input()

group = re.search(r'([a-zA-Z0-9])\1+', s)
print(group.group(1) if group else -1)

# Re.findall() & Re.finditer()

v = "[aeiou]"
c = "[qwrtypsdfghjklzxcvbnm]"
s = input()

regex = r'(?<='+c+')('+v+'{2,})'+c
f = re.findall(regex, s, re.I)

print('\n'.join(f or['-1']))

# re.start() & re.end()

s, p = input(), input()

# if p in s:
#     print(*[(i.start(), (i.start()+len(p)-1)) for i in re.finditer(r'(?={})'.format(p), s)], sep='\n')
# else:
#     print('(-1, -1)')

matches = list(re.finditer(r'(?={})'.format(p), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(p) - 1)) for match in matches))
else:
    print('(-1, -1)')

# Validating Roman Numerals

regex_pattern = r"^M{0,3}(?:C[MD]|D?C{0,3})(?:X[CL]|L?X{0,3})(?:I[XV]|V?I{0,3})$"