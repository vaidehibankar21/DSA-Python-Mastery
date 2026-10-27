class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = defaultdict(list)
        for num, count in freq.items():
            buckets[count].append(num)
        
        result = []
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) ==  k:
                    return result
        
        return result

## Time: O(n) — counting, building buckets, and scanning the frequency range take linear time overall.

## Space: O(n) — the frequency dictionary, buckets, and result require at most linear space.

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        min_heap = []
        for num, count in freq.items():
            heapq.heappush(min_heap, (count, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for count, num in min_heap]
"""

"""
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return [
            num for num, count in
            heapq.nlargest(k, freq.items(), key=lambda item: item[1])
        ]
"""

# Time: O(n + mlog k) typically for selecting the top k elements.

# Space: Up to O(m) for the frequency map and selection data.