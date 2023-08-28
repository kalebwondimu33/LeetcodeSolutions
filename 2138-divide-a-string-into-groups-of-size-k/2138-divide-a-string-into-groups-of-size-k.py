class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result=[]
        res=""
        for i in s:
            res+=i
            if len(res)==k:
                result.append(res)
                res=""
        if res:
            diff=k-len(res)
            res+=fill*diff
            result.append(res)
        return result
            
        