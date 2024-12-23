import sys
"""
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표
$(x_1, y_1)$와 백승환의 좌표
$(x_2, y_2)$가 주어지고, 조규현이 계산한 류재명과의 거리
$r_1$과 백승환이 계산한 류재명과의 거리
$r_2$가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수
$T$가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.

한 줄에 공백으로 구분 된 여섯 정수
$x_1$,
$y_1$,
$r_1$,
$x_2$,
$y_2$,
$r_2$가 주어진다.

각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는
$-1$ 출력한다.
"""

case_counts = sys.stdin.readline()

for count in range(int(case_counts)):
    case = sys.stdin.readline().split()
    x1 = int(case[0])
    y1 = int(case[1])
    r1 = int(case[2])
    x2 = int(case[3])
    y2 = int(case[4])
    r2 = int(case[5])
    dist = (((x1-x2)**2) + ((y1-y2)**2))**(1/2)
    big_r = max(r1,r2)
    small_r = min(r1,r2)
    if dist == 0 and r1==r2:
        print(-1)
    elif dist == big_r + small_r or dist == big_r - small_r:
        print(1)
    elif (big_r - small_r) < dist < (big_r + small_r):
        print(2)
    else:
        print(0)