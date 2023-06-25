class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap={}
        for i,j in paths:
            hashmap[i]=j
        for i,j in paths:
            if j not in hashmap:
                return j
        