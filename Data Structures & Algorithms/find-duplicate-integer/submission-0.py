class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        #n=len(nums)-1 because n+1 integers and range 1,n
        slow=0
        fast=0

        while True :
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break
        slow=0
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]

        return slow
        






