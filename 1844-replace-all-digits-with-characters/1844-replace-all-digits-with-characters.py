class Solution:
    def replaceDigits(self, s: str) -> str:
        alpa=string.ascii_lowercase
        result=""
        for i in range(len(s)):
            if s[i].isdigit():
                digit=s[i]
                temp=s[i-1]
                index=alpa.index(temp)
                new_ind=index+int(digit)
                result+=alpa[new_ind]
            else:
                result+=s[i]
        return result
        