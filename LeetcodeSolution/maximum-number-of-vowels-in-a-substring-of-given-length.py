class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        vowel={'a','e','i','o','u'}
        for i in range(k):
            if s[i] in vowel:
                count+=1
        curr=count
        l=0
        r=k
        while l<r and r<len(s):
            if s[l] in vowel:
                curr-=1
            if s[r] in vowel:
                curr+=1
            count=max(curr,count)
            l+=1
            r+=1
        return count

        