class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            first=num//10
            second=num%10
            num=first+second
        return num
        