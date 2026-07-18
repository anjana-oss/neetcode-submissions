class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        length=float("inf")
        total=0
        for j in range(len(nums)):
            total+=nums[j]
            while total>=target:
                length=min(length,j-i+1)
                total-=nums[i]
                i+=1
            
        return 0 if length==float("inf") else length
