class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        length=0

        for i in nums:
            if i==1:
                count+=1
                length=max(length,count)
            else:
                count=0
        return length