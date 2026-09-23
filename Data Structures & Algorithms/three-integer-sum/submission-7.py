class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            k = i+1
            j = len(nums)-1
            while k < j:
                if nums[k] + nums[j] == -nums[i]:
                    ans.append([nums[i],nums[k],nums[j]])
                    k+=1
                    j -= 1
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1
                elif nums[k] + nums[j] > -nums[i]:
                    j-=1
                elif nums[k] + nums[j] < -nums[i]:   
                    k+=1
        return ans    
        

 

