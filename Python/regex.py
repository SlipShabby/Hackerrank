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
    
import re

for i in range(int(input())):
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))

# re.split()

regex_pattern = r"[.\,]"

# group()

s = input()

group = re.search(r'([a-zA-Z0-9])\1+', s)
print(group.group(1) if group else -1)