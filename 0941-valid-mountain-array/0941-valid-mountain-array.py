class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<=2:
            return False
        gre=arr.index(max(arr))
        left=gre-1
        right=gre+1
        if gre==0 or gre==len(arr)-1:
            return False
        while  right<len(arr):
            if arr[right-1]>arr[right]:
                right+=1
            else:
                return False
        while left>=0:
            if arr[left+1]>arr[left]:
                left-=1
            else:
                return False
        return True
                
                
        