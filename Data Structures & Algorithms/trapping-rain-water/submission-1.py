class Solution:
    def trap(self, height: List[int]) -> int:
        Lmax = [-1] * len(height)
        Rmax = [-1] * len(height)
        currmax = -1
        for i in range(len(height)):
            currmax = max(currmax,height[i])
            Lmax[i] = currmax
        currmax = -1
        for j in range(len(height)-1 , -1, -1):
            currmax = max(currmax,height[j])
            Rmax[j] = currmax
        sumWater = 0
        for i in range(len(height)):
            sumWater +=  min(Lmax[i],Rmax[i]) - height[i]
        return sumWater


        