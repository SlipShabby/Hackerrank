# detect float num

# Enter your code here. Read input from STDIN. Print output to STDOUT

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

