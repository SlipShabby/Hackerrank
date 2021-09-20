
# swap case
def swap_case(s):
    return ''.join([c.upper() if c.islower() else c.lower() for c in s])


# split& join
def split_and_join(line):
    # write your code here
        return('-'.join(line.split(' ')))


# your name
def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

# mutations
def mutate_string(s, i, c):
    return (s[:i]+c+s[i+1:])

# find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if sub_string in string[i:i+len(sub_string)]:
            count +=1
    return count

# str validation
if __name__ == '__main__':
    s = str(input())
    l = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    
for check in l:
    print(any(check(c) for c in s))

# text alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# text wrap
def wrap(string, w):
    s = ""
    for i in range (0,len(string),w):
            s += string[i:i+w] + '\n'
    return s


# designer door mat
n, m = map(int,input().split()) 

def design(n,m):
    pattern = ".|."
    message = "WELCOME"
    p = [(pattern*(2*i+1)).center(m,"-") for i in range(n//2)]
    # print(p)
    print('\n'.join(p + [message.center(m, '-')] + p[::-1]))
    # for i in range(0,n-1,2):
    #     print((".|."*(i+1)).center(m,"-"))
    # print(message.center(m, "-"))
    # for i in range(n-2,0,-2):
    #     print((".|."*i).center(m,"-"))
            
design(n,m)

# string formatting
def print_formatted(number):
    for i in range(1,n+1):
        print('{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}'.format(i, w= len("{0:b}".format(n))))

# alphabet ragnoli
import string

def print_rangoli(size):
    # your code goes here
    abc =string.ascii_lowercase
    w = n*4-3
    
    for i in range(n-1,0,-1):
        s = '-'.join(abc[i:n])
        print((s[::-1]+s[1::]).center(w,'-'))
    for i in range(0,n):
        s = '-'.join(abc[i:n])
        print((s[::-1]+s[1:]).center(w,'-'))

# capitalize
def solve(string):
    ret = ""
    for i in string.split(' '):
        ret += i.capitalize() + " "
    return ret[:-1]

# Minion game
from itertools import permutations

def minion_game(string):
    # your code goes here
    vowels= 'AEIOU'
    l = len(string)
    n_subs = int(l * (l + 1) / 2)
    k = sum(l - i for i in range(l) if string[i] in vowels)   
    s = n_subs - k

    if s > k:
        print(f"Stuart {s}")
    elif s < k:
        print(f"Kevin {k}")
    else:
        print("Draw")
    
    
# merge the tools

def merge_the_tools(string, k):
    # your code goes here
    comb = [string[i:i+k] for i in range(0,len(string),k)]

    for i in range(len(comb)):
        print(''.join(dict.fromkeys(list(comb[i]))))
    











