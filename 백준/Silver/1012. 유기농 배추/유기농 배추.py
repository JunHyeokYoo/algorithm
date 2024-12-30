import sys

sys.setrecursionlimit(10**9)

def a_c(m,n,M,N):
    if m < 0 or n < 0 or m > M or n > N: # 범위 벗어남
        return
    if [m,n] in checked: # 이미 확인함
        return
    if [m,n] not in baechu: # 배추가 없음
        return
    if [m,n] in baechu: # 배추가 있으므로 위아래 양옆 확인
        checked.append([m,n])
        a_c(m+1, n, M, N)
        a_c(m-1, n, M, N)
        a_c(m, n+1, M, N)
        a_c(m, n-1, M, N)
        return True

T = int(sys.stdin.readline())

for t in range(T):

    M,N,K = map(int,(sys.stdin.readline().split()))

    baechu = []
    checked = []
    answer = 0

    for k in range(K):
        x, y = map(int,(sys.stdin.readline().split()))
        baechu.append([x,y])

    for m in range(M):
        for n in range(N):
            if a_c(m,n,M,N):
                answer += 1

    print(answer)