# map and lambda

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

        
    # return a list of fibonacci numbers

# reduce 

def product(fracs):
    t = reduce((lambda x,y: x*y) ,fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator


# validate email with filter

import re

def fun(email):
    # try:
    #     username, mail = email.split("@")
    #     website, domain = mail.split(".")
    # except ValueError:
    #     return False
    
    # if not username.replace("-", "").replace("_", "").isalnum():
    #     return False
    # if not website.isalnum():
    #     return False
    # if len(domain) > 3:
    #     return False
    # return True

    regex = r"^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[a-zA-Z]{0,3}$"     

    if not re.match(regex, email):
        return False
    return True
    
  



