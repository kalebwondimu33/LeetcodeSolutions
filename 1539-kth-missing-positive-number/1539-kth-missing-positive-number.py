class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count=1
        ans=[]
        lar=max(arr)
        left=0
        while left<len(arr):
            if count!=arr[left] and count<arr[left]:
                ans.append(count)
                count+=1
            elif count==arr[left]:
                left+=1
                count+=1
        j=1
        for i in range(k):
            ans.append(lar+j)
            j+=1
        return ans[k-1]
            
            
            
        