class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result=[]
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(nums)//2):
            result.append(even[i])
            result.append(odd[i])
        return result
