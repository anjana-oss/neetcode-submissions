class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)#shiups strength(ship can carry 10 packages )
        r=sum(weights)#or shp can carry altogether its between these 2
        res=r#its biggest working answer and we try to fimnd smaller 
        days_used=0

        while l<=r:
            mid=(l+r)//2
            currweight=0
            days_used=1

            for weight in weights:
                if currweight+weight>mid:
                    days_used+=1
                    currweight=0
                currweight+=weight
            if days_used<=days:
                res=mid#mid works
                r=mid-1#find smaller
            else:
                l=mid+1
        return res 