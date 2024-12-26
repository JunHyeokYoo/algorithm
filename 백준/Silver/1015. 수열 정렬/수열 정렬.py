import sys

N = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

sort_A = sorted(A)

answer = []

for i in A:
    index = sort_A.index(i)
    answer.append(index)
    sort_A[index] = -1

answer = map(str,answer)
print(" ".join(answer))