class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left=0
        odd=0
        arr=[]
        prev=0
        i=0
        count=0
        for right in range(len(nums)):
            if nums[right]%2!=0:
                arr.append(right)
                odd+=1
            if odd>k:
                prev=arr[i]+1
                odd-=1
                i+=1
            if odd==k:
                count+=(arr[i]-prev+1)
        return count
            



