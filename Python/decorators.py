# Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
    return fun


# name directory

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key = lambda x: int(x[2])))
        # complete the function
    return inner

