class Solution:
    def isPalindrome(self, s: str) -> bool:
        output=""
        for i in s:
            if i.isalnum():
                output+=i.lower()
        left=0
        right=len(output)-1
        while left<right:
            if output[left]==output[right]:
                left+=1
                right-=1
            else:
                return False
        return True