class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        max_area = 0

        # Area for two nums heights[i] and heights[j] (where j>i) is (j-i) * min(hieght[i], height[j])
        i=0
        j = 1
        while i < len(heights)-1:
            area = (j-i)*min(heights[j], heights[i])
            max_area = max(area, max_area)
            j+=1
            if j == len(heights):
                i+=1
                
                j=i+1
        
        # [2, 1]
        return max_area
