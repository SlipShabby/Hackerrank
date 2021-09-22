# exceptions

for i in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except BaseException as err:
        print(f"Error Code: {err}")

# incorrect regex

import re

for i in range(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')

