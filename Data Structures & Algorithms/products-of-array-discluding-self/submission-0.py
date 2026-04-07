class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mul = 1
        r_mul = 1
        n = len(nums)
        l_nums = [1] * n
        r_nums = [1] * n
        for i in range(n):
            j = -i -1
            l_nums[i] = l_mul
            r_nums[j] = r_mul
            l_mul *= nums[i]
            r_mul *= nums[j]

        return [l*r for l,r in zip(l_nums,r_nums)]