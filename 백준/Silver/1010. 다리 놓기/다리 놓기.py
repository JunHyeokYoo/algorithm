import sys

case_count = int(sys.stdin.readline())

for case in range(case_count):
    N, M = map(int,sys.stdin.readline().split())
    child = 1
    parant = 1
    for m in range(M, M - N , -1):
        child *= m
    for n in range(N,1,-1):
        parant *= n
    answer = child / parant
    print(int(answer))