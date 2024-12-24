import sys
"""
위와 같은 은하수 지도, 출발점, 도착점이 주어졌을 때 어린 왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자. 행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다. 또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.
"""

def is_in_r(cx,cy,r,x,y):
    dist = ((cx-x)**2 + (cy-y)**2)**(0.5)
    if dist < r:
        return True
    else:
        return False

case_counts = int(sys.stdin.readline())

for case in range(case_counts):
    answer = 0
    coor = sys.stdin.readline().split()
    x1, y1, x2, y2 = map(int, coor)
    r_counts = int(sys.stdin.readline())
    for r_count in range(r_counts):
        r_xyr = sys.stdin.readline().split()
        cx, cy, r = map(int, r_xyr)
        if is_in_r(cx, cy, r, x1, y1) ^ is_in_r(cx, cy, r, x2, y2): # 두점중 한점만 포함할때
            answer += 1

    print(answer)