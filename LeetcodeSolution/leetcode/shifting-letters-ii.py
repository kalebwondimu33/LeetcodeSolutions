class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp=[0]*len(s)
        sign=0
        for start,end,dire in shifts:
            if dire==0:
                sign=-1
            else:
                sign=1
            temp[start]+=1*sign
            if end+1<len(temp):
                temp[end+1]-=1*sign
        ans=""
        pref=0
        for i in range(len(s)):
            char=ord(s[i])
            pref+=temp[i]
            pref=pref%26
            if pref<0:
                ans+=chr((char-97+pref+26)%26+97)
            else:
                ans+=chr((char-97+pref)%26+97)
            
        return ans



        