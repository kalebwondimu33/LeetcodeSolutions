class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique=len(set(nums))
        count=0
        print(unique)
        for i in range(len(nums)):
            dct=defaultdict(int)
            dct[nums[i]]+=1
            if len(dct)==unique:
                count+=1
            for j in range(i+1,len(nums)):
                dct[nums[j]]+=1
                if len(dct)==unique:
                    count+=1
        return count

                


        


            

        