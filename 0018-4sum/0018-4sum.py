class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer=[]
        nums.sort()
        d={}
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                l=j+1
                r=len(nums)-1
                while l<r:
                    if nums[i]+nums[j]+nums[l]+nums[r]==target:
                        
                        if f"{nums[i]}{nums[j]}{nums[l]}{nums[r]}" not in d:
                            d[f"{nums[i]}{nums[j]}{nums[l]}{nums[r]}" ]=1
                            answer.append([nums[i],nums[j],nums[l],nums[r]])
                            
                            
                            
                        
                        l+=1
                    elif nums[i]+nums[j]+nums[l]+nums[r]>target:
                        r-=1
                    else:
                        l+=1
        return answer
                