class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        before=0
        for i in spaces:
            ans.append(s[before:i])
            before=i
        ans.append(s[before:])
        return ' '.join(ans)
        