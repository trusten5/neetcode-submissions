class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        i=0
        j = len(heights)-1
        while i<j:
            area = max(area, (j-i)*min(heights[j], heights[i]))
            if heights[j]<heights[i]:
                j-=1
            else:
                i+=1
        
        return area