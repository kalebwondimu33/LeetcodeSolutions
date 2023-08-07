class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result=[]
        for i in words:
            for j in i.split(separator):
                if j:
                    result.append(j)
        return result
                
            
        