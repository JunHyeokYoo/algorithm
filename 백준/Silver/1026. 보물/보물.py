import sys

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))

answer = 0

for n in range(N):
    min_A = min(A)
    max_B = max(B)
    answer += min_A * max_B
    min_A_index = A.index(min_A)
    max_B_index = B.index(max_B)

    A.pop(min_A_index)
    B.pop(max_B_index)
print(answer)