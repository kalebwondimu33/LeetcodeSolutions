class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        leng=len(s)
        vowel="aioue"
        a=s[:leng//2].lower()
        b=s[leng//2:].lower()
        count1=0
        count2=0
        for i in a:
            if i in vowel:
                count1+=1
        for i in b:
            if i in vowel:
                count2+=1
        if count1==count2:
            return True
        else:
            return False
        