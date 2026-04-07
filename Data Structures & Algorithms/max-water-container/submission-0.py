class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        h = len(heights)-1
        ans = 0
        while l <h:
            if heights[l]<heights[h]:
                lenght = h - l
                area = heights[l] * lenght
                ans = max(ans,area)
                l +=1
            else:
                lenght = h - l 
                area = heights[h] * lenght
                ans = max(ans,area)
                h -=1

        return ans


