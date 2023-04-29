class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        count=0
        for i in s.split():
            if i.isdigit()and int(i)<=count:
                return False
            elif i.isdigit():
                count=int(i)
        return True
    
        
                
        