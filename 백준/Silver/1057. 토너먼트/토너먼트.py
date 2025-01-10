import math
import sys

N , K, I = map(int,sys.stdin.readline().split())
round = 0
while K != I:
    round+=1
    K = (K+1) // 2
    I = (I+1) // 2

print(round)