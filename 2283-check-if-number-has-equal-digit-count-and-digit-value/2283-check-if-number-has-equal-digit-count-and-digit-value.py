class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if num[i]!=str(num.count(f"{i}")):
                return False
        return True
                
        