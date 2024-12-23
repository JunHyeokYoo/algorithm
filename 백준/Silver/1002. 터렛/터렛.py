import sys, math
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

for _ in range(int(case_counts)):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    # 1) 거리 계산은 float(실수)로 해야 함
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if distance == 0 and r1 == r2:          # 동심원 & 반지름이 같은 경우
        print(-1)
    elif abs(r1 - r2) == distance or (r1 + r2) == distance:  # 내접 or 외접
        print(1)
    elif abs(r1 - r2) < distance < (r1 + r2): # 두 점에서 만나는 경우
        print(2)
    else:                                    # 그 외
        print(0)