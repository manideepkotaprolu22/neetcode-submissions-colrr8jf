class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxSum , currSum = nums[0],0
        for i,num in enumerate(nums):
            if currSum < 0:
                currSum = 0
            currSum += num
            mxSum = max(currSum,mxSum)
        return mxSum    

        