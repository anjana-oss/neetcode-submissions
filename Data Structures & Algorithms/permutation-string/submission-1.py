class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count={}
        for i in range(len(s1)):
            if s1[i] not in count:
                count[s1[i]]=1
            else:

                count[s1[i]]+=1
        i=0
        k=len(s1)
        map={} 
        for j in range(len(s2)):
            if s2[j] not in map:
                    map[s2[j]]=1
            else:

                map[s2[j]]+=1

            if j-i+1>k:
                map[s2[i]]-=1
                if map[s2[i]]==0:
                    del map[s2[i]]
                i+=1
            if  j-i+1==k:
               
                if map==count:
                    return True
            
        return False

