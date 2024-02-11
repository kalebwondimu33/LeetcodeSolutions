class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n,visted=len(nums),set()
        for i in range(n):
            if i not in visted:
                circle=set()
                while True:
                    if i in circle:
                        return True
                    if i in visted:
                        break
                    visted.add(i)
                    circle.add(i)
                    prev,i=i,(i+nums[i])%n
                    if prev==i or (nums[prev]>0) != (nums[i]>0):
                        break


              
        return False

        
        

            
        