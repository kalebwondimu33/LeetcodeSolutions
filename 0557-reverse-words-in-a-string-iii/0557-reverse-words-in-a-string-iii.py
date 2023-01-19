class Solution:
    def reverseWords(self, s: str) -> str:
        result=""
        results=s.split()
        for i in results:
            result=result+i[::-1]+" "
        return result.rstrip()
        