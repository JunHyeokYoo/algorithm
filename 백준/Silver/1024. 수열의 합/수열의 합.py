import sys

N , L = map(int,sys.stdin.readline().split())

for length in range(L, 101):
    temp_sum = length * (length - 1 ) // 2
    if N - temp_sum < 0:
        break

    if ( N - temp_sum ) % length == 0:
        start = (N - temp_sum) // length
        if start < 0:
            continue

        answer = [start + i for i in range(length)]

        print(" ".join(map(str, answer)))
        exit()
print(-1)