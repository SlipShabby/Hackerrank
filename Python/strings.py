
# swap case

def swap_case(s):
    return ''.join([c.upper() if c.islower() else c.lower() for c in s])


# split& join

def split_and_join(line):
    # write your code here
        return('-'.join(line.split(' ')))


