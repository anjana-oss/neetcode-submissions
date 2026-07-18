class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close={')':'(','}':'{',']':'['}
        for str in s:
            if str in close:
                if stack and stack[-1]==close[str]:
                     stack.pop()
                else:
                    return False
            else:
                stack.append(str)
        if not stack:
            return True
        else:
             return False