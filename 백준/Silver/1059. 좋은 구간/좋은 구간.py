import sys

L = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
n = int(sys.stdin.readline())

# n이 이미 집합 S에 속해 있다면 좋은 구간은 불가능
if n in n_list:
    print(0)

else:

    # n보다 작은 S 원소 중 최댓값(small_val), 없는 경우 0 또는 1 이하인 경우 등 처리
    small_val = 0
    for x in n_list:
        if x < n:
            small_val = x
        else:
            break

    # n보다 큰 S 원소 중 최솟값(big_val), 없는 경우 처리
    big_val = 0
    for x in n_list:
        if x > n:
            big_val = x
            break

    left_gap = n - small_val
    right_gap = big_val - n
    # A < B 이어야 하므로, (left_gap * right_gap)에서
    # "A=B=n" 인 1개를 빼준다.
    answer = left_gap * right_gap - 1

    print(answer)