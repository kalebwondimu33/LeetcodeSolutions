class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        seen = {}
        for item in nums:
            if item % 2 ==0:
                seen[item] = 1 if item not in seen else seen[item] + 1
        maxx = 0    
        output = -1        
        for num, count in seen.items():
            if count > maxx:
                maxx, output = count, num
            elif count == maxx:
                output = min(num,output)
        return output
        
                
            
        
        