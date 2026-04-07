from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_items[i][0])

        return res
