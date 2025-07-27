import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, user, score):
        heapq.heappush(self.heap, (-score, user))

    def extract_top_k(self, k):
        return [heapq.heappop(self.heap) for _ in range(min(k, len(self.heap)))]
