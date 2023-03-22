class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable={}
        maxx=0
        start=0
        for i in range(len(s)):
            current=s[i]
            if current in hashtable:
                start=max(start,hashtable[current]+1)
            length=(i-start)+1
            maxx=max(maxx,length)
            hashtable[current]=i
        return maxx
        
        