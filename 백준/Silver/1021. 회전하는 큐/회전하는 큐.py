import sys

N, M = map(int,sys.stdin.readline().split())

queue = []

for n in range(1,N+1):
    queue.append(n)

indices = map(int,sys.stdin.readline().split())

def left(arr):
    return arr[1:] + arr[:1]

def right(arr):
    return arr[-1:] + arr[:-1]

answer = 0

for index in indices: # 찾으려는 정수 순서대로 찾기
    while(queue[0] != index): # 현재 큐에서 뽑기 불가능 하면 돌려야함
        if queue.index(index) <= len(queue)/2: # 찾으려는 값이 현재 큐 길이 절반중 앞에 있으면
            queue = left(queue)
            answer += 1
        else:
            queue = right(queue)
            answer += 1
    queue.pop(0) #뽑기

print(answer)