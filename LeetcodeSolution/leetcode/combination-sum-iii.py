class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(index,path):
            if sum(path)==n and len(path)==k:
                result.append(path[:])
                return 
            if len(path)>=k:
                return 
            for i in range(index,10):
                path.append(i)
                backtrack(i+1,path)
                path.pop()
        result=[]
        backtrack(1,[])
        return result
        

        