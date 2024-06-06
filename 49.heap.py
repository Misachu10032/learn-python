import heapq

heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 6)
heapq.heappush(heap, 8)
# heapq.heappush(heap, 9)

print(heap)  # Output: [3, 7, 5, 10]