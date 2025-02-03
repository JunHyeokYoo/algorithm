import heapq

X = int(input())

sum_sticks = 64
heap = [64]
heapq.heapify(heap)

while sum_sticks > X:
    min_stick = heapq.heappop(heap)
    sum_sticks -= min_stick

    half = min_stick // 2

    temp_sum = sum_sticks + half * 2

    if (temp_sum - half) >= X:
        sum_sticks = temp_sum - half
        heapq.heappush(heap, half)
    else:
        sum_sticks = temp_sum
        heapq.heappush(heap, half)
        heapq.heappush(heap, half)

print(len(heap))