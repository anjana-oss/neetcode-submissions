class Solution:
    def maxArea(self, heights: List[int]) -> int:
       i=0
       maxarea=0
       j=len(heights)-1
       while i<j:
        width=j-i
        area1=min(heights[i],heights[j])*width
        maxarea=max(maxarea,area1)
        if heights[i]<heights[j]:
            i+=1
        else:
            j-=1
       return maxarea