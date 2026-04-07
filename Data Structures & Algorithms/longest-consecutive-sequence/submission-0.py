class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest= 0
        s = set(nums)
        
        for num in s:
            if num-1 not in s:
                num_next = num + 1
                current = 1
                while num_next in s:    
                    num_next += 1
                    current +=1
                longest= max(longest, current )
        return longest 

        