from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: sort array
        nums.sort()

        # Step 2: build frequency dictionary
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 3: sort dictionary by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 4: take top k frequent elements
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])

        return res
