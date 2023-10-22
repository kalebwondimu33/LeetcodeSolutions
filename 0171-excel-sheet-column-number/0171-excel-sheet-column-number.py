class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        pos,ans=0,0
        for i in reversed(columnTitle):
            digit=ord(i)-64
            ans+=digit*26**pos
            pos+=1
        return ans
    
    
    
        