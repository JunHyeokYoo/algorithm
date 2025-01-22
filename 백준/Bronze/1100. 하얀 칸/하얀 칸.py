# 체스판 상태 입력 받기
chessboard = [input() for _ in range(8)]

# 하얀 칸 위에 있는 말(F)의 개수 세기
count = 0
for i in range(8):
    for j in range(8):
        # 하얀 칸은 (i + j) % 2 == 0으로 구분됨
        if (i + j) % 2 == 0 and chessboard[i][j] == 'F':
            count += 1

# 결과 출력
print(count)