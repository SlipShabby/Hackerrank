
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



