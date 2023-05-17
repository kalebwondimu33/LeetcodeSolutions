class Solution:
    def reverseVowels(self, s: str) -> str:
        result=[]
        left=0
        right=len(s)-1
        for i in s:
            result.append(i)
        while left<right:
            if result[left] in "aeiouAEIOU" and result[right] in "aeiouAEIOU":
                result[left],result[right]=result[right],result[left]
                left+=1
                right-=1
            elif result[left] in "aeiouAEIOU":
                right-=1
            else:
                left+=1
        return "".join(result)
                
        