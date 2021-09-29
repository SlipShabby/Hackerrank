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

# validating phone numbers

for i in range(int(input())):
    if re.match(r'[789]\d{9}$',input()):   
        print('YES')  
    else:  
        print('NO')  

# Validating and Parsing Email Addresses

import email.utils

for i in range(int(input())):
    
    name, mail = map(str,email.utils.parseaddr(input()))
    
    validEmail = re.search(r'^[a-zA-Z]+[a-zA-Z0-9_.-]+[@][a-zA-Z]+[.][a-zA-Z]{1,3}$', mail)
   
    if validEmail:
        print(email.utils.formataddr((name, mail)))


# hex color code

# pattern=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
pattern = r'(?<!^)(#(?:[\da-f]{3}){1,2})'
for i in range(int(input())):
    for x in re.findall(pattern,input(), re.I):
        print(x)

# HTML Parser 1

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for ele in attrs:
            print ('->',ele[0],'>',ele[1])

# instantiate the parser and fed it some HTML

            
parser = MyHTMLParser()
parser.feed(''.join([input().strip() for _ in range(int(input()))]))


# HTML Parser 2

from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_comment(self, data):
#         n = len(data.split('\n'))
#         if n > 1:
#             print(">>> Multi-line Comment")
#         else:
#             print(">>> Single-line Comment")
#         if data.strip():
#             print(data)
          
#     def handle_data(self, data):
#         if data.strip():
#             print(">>> Data")
#             print(data)
  

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            comment = 'Multi'
        else:
            comment = 'Single'
        print(f'>>> {comment}-line Comment\n{data.strip()}')
  
    def handle_data(self, data):
        if data != '\n':
            print(f'>>> Data\n{data}')

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# detect HTML tags

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

