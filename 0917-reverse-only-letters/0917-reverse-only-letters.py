class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left=0
        right=len(s)-1
        result=[]
        for i in s:
            result.append(i)
        while left<right:
            if result[left].isalpha() and result[right].isalpha():
                result[left],result[right]=result[right],result[left]
                left+=1
                right-=1
            elif result[left].isalpha() and result[right].isalpha()==False:
                right-=1
            elif result[left].isalpha()==False and result[right].isalpha():
                left+=1
            else:
                left+=1
                right-=1
        return "".join(result)
                
        