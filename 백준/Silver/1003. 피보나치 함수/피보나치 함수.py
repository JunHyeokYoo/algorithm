import sys

T = int(sys.stdin.readline())

# DP 테이블 초기화
# dp[i]는 (0 호출 횟수, 1 호출 횟수)
dp = [(1, 0), (0, 1)]  # fibo(0), fibo(1)

# 미리 피보나치 호출 횟수를 계산 (최대 40으로 가정)
for i in range(2, 41):
    dp.append((dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]))

# 입력 처리 및 결과 출력
for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N][0], dp[N][1])