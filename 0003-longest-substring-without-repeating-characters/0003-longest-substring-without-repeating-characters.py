class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        maxx=0
        start=0
        for i in range(len(s)):
            current=s[i]
            if current in d:
                start=max(start,d[current]+1)
            length=(i-start)+1
            maxx=max(maxx,length)
            d[current]=i
        return maxx
        