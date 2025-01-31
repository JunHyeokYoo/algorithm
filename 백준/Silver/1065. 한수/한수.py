import sys

N = int(sys.stdin.readline().strip())

def is_hansu(num: int) -> bool:
    if num < 100:
        return True
    
    # 세 자리 이상
    digits = list(map(int, str(num)))
    
    diff = digits[1] - digits[0]
    for i in range(1, len(digits)-1):
        if digits[i+1] - digits[i] != diff:
            return False
    return True

count = 0
for x in range(1, N+1):
    if is_hansu(x):
        count += 1

print(count)