class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic={}
        result=""
        for i in range(len(indices)):
            dic[indices[i]]=s[i]
        for i in range(len(dic)):
            result+=dic[i]
        return result
            