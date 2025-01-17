import math

T = int(input().strip())

for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x

    if distance == 0:
        print(0)
        continue

    n = int(math.isqrt(distance))  # 정수 제곱근

    if n * n == distance:
        print(2 * n - 1)
    elif distance <= n * n + n:
        print(2 * n)
    else:
        print(2 * n + 1)