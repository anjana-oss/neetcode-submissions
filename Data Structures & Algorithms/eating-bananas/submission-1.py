class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 #because slowest kok can eat banana is 1/hr
        r=max(piles) 
        while l<=r:
            mid=(l+r)//2#k

            total=0
            for pile in piles:

                total+=math.ceil(pile/mid)#pile/k(4/2)=2(need 2 hours) ceil=2.1->3(round to big integer)
            if total<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
             
        return res
                
