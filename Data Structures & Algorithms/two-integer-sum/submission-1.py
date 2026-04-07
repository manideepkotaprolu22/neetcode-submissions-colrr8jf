class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in dict and i!=dict[val]:
                return [i,dict[val]]
                
