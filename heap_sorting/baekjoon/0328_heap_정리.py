## heap

import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

print(heapq.heappop(heap))
print(heap)

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)
print(heap[0])


### 최대힙
## 앞에 음수를 넣어서 튜플로 입력 때리기
## 값이 클수록 앞에 음수값은 작아질테니 --> 최소힙 역으로 이용~!

import heapq

nums = [4, 1, 7, 3, 8, 5]
min_heap = []
for num in nums:
    heapq.heappush(min_heap, num)

print(min_heap)
while min_heap:
    print(heapq.heappop(min_heap))

print("------------------- ")

max_heap = []
for num in nums:
    heapq.heappush(max_heap, (-num, num))  # (우선 순위, 값)

print(max_heap)
while max_heap:
    print(heapq.heappop(max_heap)[1])


## 절대값 힙
nums = [4, 1, 7, 3, -8, 5,-3]
abs_heap = []
for num in nums:
    heapq.heappush(abs_heap,(abs(num),num))

print("==============")
print(abs_heap)


