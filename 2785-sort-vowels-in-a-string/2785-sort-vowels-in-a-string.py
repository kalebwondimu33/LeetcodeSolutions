class Solution:
    def sortVowels(self, s: str) -> str:
        vowel=[]
        ans=""
        for i in s:
            if i.lower() in "aeiou":
                vowel.append(i)
        vowel=sorted(vowel)
        left=0
        right=0
        while right<len(s):
            if s[right].lower() in "aeiou":
                ans+=vowel[left]
                left+=1
                right+=1
            else:
                ans+=s[right]
                right+=1
        return ans
        