class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic={}
        total=0
        start=0
        arr=[]
        curr=0
        maxx=0
        all_sum=0
        for i in range(len(nums)):
            curr+=nums[i]
            arr.append(curr)

        for right in range(len(nums)):
            total+=nums[right]
            all_sum+=nums[right]
            if nums[right] in dic:
                if start<dic[nums[right]]+1:
                    start=dic[nums[right]]+1
                    total=all_sum-arr[dic[nums[right]]]
            maxx=max(total,maxx)
            dic[nums[right]]=right

        return maxx

        