class Solution:
    def reverseWords(self, s: str) -> str:
        result=s.split()
        for i in range(len(result)):
            if result[i]==" ":
                result[i]=""
        ans=list(reversed(result))
        return ' '.join(ans)
        