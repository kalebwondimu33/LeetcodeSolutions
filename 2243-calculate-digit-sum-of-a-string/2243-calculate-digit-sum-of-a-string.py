class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            set_s=[s[i:i+k] for i in range(0,len(s),k)]
            s=''
            for e in set_s:
                s+=str(sum(map(int,e)))
        return s
            
        