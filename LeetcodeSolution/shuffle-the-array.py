class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        length=(n*2)//2
        for i in range(length):
            ans.append(nums[i])
            ans.append(nums[i+length])
        return ans
        