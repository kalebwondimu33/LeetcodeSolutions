class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front=[]
        back=[0]*len(nums)
        temp=1
        ans=[]
        for num in nums:
            temp*=num
            front.append(temp)
        curr=1
        for i in range(len(nums)-1,-1,-1):
            curr*=nums[i]
            back[i]=curr
        for j in range(len(nums)):
            if j==0:
                ans.append(back[j+1])
            elif j>0 and j<len(nums)-1:
                ans.append(front[j-1]*back[j+1])
            else:
                ans.append(front[j-1])
        return ans

        