class Solution:
    def reverseWords(self, s: str) -> str:
        result=s.split()
        ans=list(reversed(result))
        return ' '.join(ans)
        