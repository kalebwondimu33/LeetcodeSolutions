class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small=[]
        large=[0]*(len(nums)-2)
        minn=nums[0]
        maxx=nums[-1]
        for i in range(1,len(nums)-1):
            small.append(minn)
            minn=min(minn,nums[i])
        for j in range(len(nums)-2,0,-1):
            large[j-1]=maxx
            maxx=max(maxx,nums[j])
        for k in range(1,len(nums)-1):
            if small[k-1]<nums[k]<large[k-1]:
                return True
        print(small)
        print(large)
        return False

            

        
        
        
        
        