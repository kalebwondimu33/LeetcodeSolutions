class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def backtrack(start, path=[]):
            if sum(path) == target:
                ans.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                
                if sum(path) + candidates[i] > target:
                    break  # Stop exploring further if sum exceeds target
                
                path.append(candidates[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0)
        return ans

# Example usage:
# solution = Solution()
# print(solution.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27))
