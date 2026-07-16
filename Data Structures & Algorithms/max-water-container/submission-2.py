class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        max_area = 0

        # Area for two nums heights[i] and heights[j] (where j>i) is (j-i) * min(hieght[i], height[j])
        i=0
        j = len(heights)-1
        while i < j:
            area = (j-i)*min(heights[j], heights[i])
            max_area = max(area, max_area)
            if heights[j] < heights[i]:
                j-=1
            else:
                i+=1

        
        # [2, 1]
        return max_area
