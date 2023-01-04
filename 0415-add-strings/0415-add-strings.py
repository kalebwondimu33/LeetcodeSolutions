class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1=len(num1)
        sum1=num1+num2
        return str(int(sum1[:nums1])+int(sum1[nums1:]))
        
            
            
        