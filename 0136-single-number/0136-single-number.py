class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        dic={v:k for k,v in count.items()}
        return dic[1]
        