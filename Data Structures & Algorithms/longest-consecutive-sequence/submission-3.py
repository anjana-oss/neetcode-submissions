class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash1=set(nums)
        seq=0
        longest=0
        for num in nums:
            if num-1 not in hash1:
                length=1
                while num+length in hash1:
                    length+=1
                longest=max(length,longest)
        return longest
                
                