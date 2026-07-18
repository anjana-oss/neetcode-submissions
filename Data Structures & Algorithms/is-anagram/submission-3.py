class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        counts,count={},{}
        for i in range(len(s)):
            counts[s[i]]=1+counts.get(s[i],0)
            count[t[i]]=1+count.get(t[i],0)
        return counts==count

            
