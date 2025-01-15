import sys

N = int(sys.stdin.readline())

mat = []

for i in range(N):
    line = list(map(lambda x : 1 if x == 'Y' else 0, sys.stdin.readline().strip()))
    mat.append(line)
# 2-친구 계산
max_answer = 0
for i in range(N):
    two_friend_set = set()  # i의 2-친구를 저장할 집합
    for j in range(N):
        if mat[i][j] == 1:  # i와 j가 직접 친구
            two_friend_set.add(j)
            for k in range(N):
                if mat[j][k] == 1 and k != i:  # j와 k가 직접 친구이고, k != i
                    two_friend_set.add(k)
    max_answer = max(max_answer, len(two_friend_set))

print(max_answer)
