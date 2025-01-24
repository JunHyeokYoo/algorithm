import math

xA, yA, xB, yB, xC, yC = map(int, input().split())

# 거리 계산 함수
def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 외적 함수 (두 벡터 (x1,y1), (x2,y2)의 cross product)
def cross(x1, y1, x2, y2):
    return x1*y2 - y1*x2

# 세 점 간 거리
AB = dist(xA, yA, xB, yB)
BC = dist(xB, yB, xC, yC)
CA = dist(xC, yC, xA, yA)

# 유효한 둘레들을 보관할 리스트
perimeters = []

ABx, ABy = (xB - xA), (yB - yA)
ACx, ACy = (xC - xA), (yC - yA)
if cross(ABx, ABy, ACx, ACy) != 0:  # 평행하지 않다면
    perimeters.append(2 * (AB + CA))

BAx, BAy = (xA - xB), (yA - yB)
BCx, BCy = (xC - xB), (yC - yB)
if cross(BAx, BAy, BCx, BCy) != 0:
    perimeters.append(2 * (AB + BC))  # |BA| = AB

CAx, CAy = (xA - xC), (yA - yC)
CBx, CBy = (xB - xC), (yB - yC)
if cross(CAx, CAy, CBx, CBy) != 0:
    perimeters.append(2 * (CA + BC))  # |CA| = CA, |CB| = BC

# 결과 출력
if len(perimeters) == 0:
    print(-1)
else:
    print(max(perimeters) - min(perimeters))