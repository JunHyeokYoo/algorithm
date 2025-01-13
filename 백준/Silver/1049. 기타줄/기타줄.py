import sys
import math

N , M = map(int,sys.stdin.readline().split())

# 최대 6 숫자
six_c = math.ceil(N/6)

all_combine = []

for i in range(six_c + 1):
    if N-i*6 <= 0:
        combine = [i , 0]
    else:
        combine = [i , N-i*6]
    all_combine.append(combine)

# print(all_combine)

all_six = []
all_one = []

for m in range(M):
    now_six , now_one = map(int,sys.stdin.readline().split())
    all_six.append(now_six)
    all_one.append(now_one)

my_six = min(all_six)
my_one = min(all_one)

answer_candidate = []

for combine in all_combine: # [0,13],[1,7],...
    answer = 0
    answer += combine[0]*my_six
    answer += combine[1]*my_one
    answer_candidate.append(answer)

print(min(answer_candidate))

