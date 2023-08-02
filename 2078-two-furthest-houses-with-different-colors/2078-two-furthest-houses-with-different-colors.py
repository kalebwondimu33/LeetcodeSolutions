class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        n=len(colors)-1
        for i in range(len(colors)-1):
            if colors[i]!=colors[-1]:
                ans=max(ans,n-i)
        for i in range(len(colors)-1,0,-1):
            if colors[i]!=colors[0]:
                ans=max(ans,i-0)
        if len(colors)%2!=0:
            i,j=len(colors)//2,len(colors)//2
            while i>=0 and j<len(colors):
                if colors[i]!=colors[j]:
                    ans=max(ans,j-i)
                i-=1
                j+=1
        if len(colors)%2==0:
            i,j=len(colors)//2,(len(colors)//2)+1
            while i>=0 and j<len(colors):
                if colors[i]!=colors[j]:
                    ans=max(ans,j-i)
                i-=1
                j+=1
        return ans
            
        