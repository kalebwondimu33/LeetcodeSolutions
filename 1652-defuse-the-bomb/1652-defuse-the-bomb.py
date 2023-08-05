class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans=[0]*len(code)
        if k==0:
            return [0]*len(code)
        elif k>0:
            for i in range(len(code)):
                for j in range(i+1,i+k+1):
                    ans[i]+=code[j%len(code)]
        else:
            for i in range(len(code)):
                l=1
                while l<=(-k):
                    temp=(i-l)%len(code)
                    ans[i]+=code[temp]
                    l+=1
        return ans
        
        