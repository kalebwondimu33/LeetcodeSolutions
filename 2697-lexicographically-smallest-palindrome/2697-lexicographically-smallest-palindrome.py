class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left=0
        nlist=list(s)
        right=len(s)-1
        while left<right:
            if nlist[left]!=nlist[right]:
                if ord(nlist[left])>ord(nlist[right]):
                    nlist[left]=nlist[right]
                    left+=1
                    right-=1
                else:
                    nlist[right]=nlist[left]
                    left+=1
                    right-=1
            else:
                left+=1
                right-=1
        return "".join(nlist)
                    
            
                    
                    
        