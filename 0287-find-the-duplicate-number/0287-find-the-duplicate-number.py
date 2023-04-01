class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare=0
        tortoise=0
        while True:
            hare=nums[nums[hare]]
            tortoise=nums[tortoise]
            if hare==tortoise:
                pointer=0
                while pointer!=tortoise:
                    pointer=nums[pointer]
                    tortoise=nums[tortoise]
                return pointer
        