class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        preM = 1
        for i in range(len(nums)):
            res[i] = preM
            preM *= nums[i]
        suf = 1    
        for j in range(n-1,-1,-1):
            res[j] *= suf
            suf *= nums[j] 
        return res

            
