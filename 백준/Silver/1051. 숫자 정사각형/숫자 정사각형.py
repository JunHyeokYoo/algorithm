import sys

N, M = map(int,sys.stdin.readline().split())

board = []
for n in range(N):
    board.append(list(map(int,sys.stdin.readline().strip())))

max_area = 1

for i in range(N):
    for j in range(M):
        max_k = min(N-1-i, M-1-j)
        for k in range(max_k + 1):
            side_length = k+1
            if (board[i][j] == board[i][j+k] == board[i+k][j] == board[i+k][j+k]):
                max_area = max(max_area, side_length ** 2)

print(max_area)