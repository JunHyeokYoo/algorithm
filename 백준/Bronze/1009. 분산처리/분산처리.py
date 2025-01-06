import sys

T = int(sys.stdin.readline())

for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    last = pow(a,b,10)
    if last == 0:
        print(10)
    else:
        print(last)