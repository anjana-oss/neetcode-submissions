class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        map={}
        dis=0

        for i in arr:
                if i in map:
                    map[i]+=1
                else:
                    map[i]=1



        for i in arr:
            if map[i]==1:
                dis+=1

                if dis==k:
                    return i
        return ""