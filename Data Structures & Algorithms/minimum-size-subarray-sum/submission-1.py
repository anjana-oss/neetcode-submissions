class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        length=float("inf")#here its minminum so take largets value dont tak 0
        total=0
        for j in range(len(nums)):
            total+=nums[j]
            while total>=target:
                length=min(length,j-i+1)
                total-=nums[i]
                i+=1
            
        if length==float("inf"):
            return 0
        else:
            return length
