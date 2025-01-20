import re

cases = int(input().strip())

pattern = re.compile(r'^(100+1+|01)+$')

# (100+1+ | 01)+
for _ in range(cases):
    patt = str(input().strip(" "))
    if pattern.fullmatch(patt):
        print("YES")
    else:
        print("NO")