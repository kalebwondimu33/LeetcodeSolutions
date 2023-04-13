class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            f=0
            l=len(i)-1
            flag=True
            while f<=l:
                if i[f]==i[l]:
                    f+=1
                    l-=1
                else:
                    flag=False
                    break
            if flag:
                return i
        return ""
            
            
        