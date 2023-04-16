class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        output=[]
        remain=0
        total=0
        if len(nums)==1:
            return [0,1]
        for i in count:
            if count[i]:
                total+=count[i]//2
                remain+=count[i]%2
        output.append(total)
        output.append(remain)
        return output
        
        
            
        