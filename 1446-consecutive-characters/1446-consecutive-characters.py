class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        res=1
        left=0
        right=1
        while left<right and right<len(s):
            if s[left]==s[right]:
                count+=1
                right+=1
                res=max(res,count)
            else:
                left=right
                right+=1
                count=1
        return res