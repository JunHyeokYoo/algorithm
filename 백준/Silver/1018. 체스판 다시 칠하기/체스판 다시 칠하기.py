import sys

N, M = map(int,sys.stdin.readline().split())


chess = []
changed_chess = [] # 변경기록 체스판

for n in range(N):
    changed_chess.append([0] * M)

for n in range(N):
    lines = sys.stdin.readline().strip()
    chess.append(lines)

first = chess[0][0]

for i in range(len(chess)):
    for j in range(len(chess[i])):
        if (i+j)%2 == 0: # i+ j 값이 짝수면 맨 첫번째 값이랑 같아야함
            if chess[i][j] != first: # 근데 다르면
                changed_chess[i][j] = 1 # 수정
        else: # i + j 값이 홀수면 맨 첫번째 값이랑 달라야함
            if chess[i][j] == first: # 근데 같으면
                changed_chess[i][j] = 1 # 수정

max_ones = 0
min_ones = float('inf')

for i in range(N-7):
    for j in range(M-7):
        one_count = 0

        for x in range(8):
            for y in range(8):
                one_count += changed_chess[i+x][j+y]
        max_ones = max(max_ones, one_count)
        min_ones = min(min_ones, one_count)

max_diff = 64-max_ones
answer = min(max_diff,min_ones)
print(answer)