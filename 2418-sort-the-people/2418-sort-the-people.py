class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={}
        result=[]
        for i in range(len(heights)):
            dic[heights[i]]=names[i]
        heights.sort(reverse=True)
        for i in heights:
            result.append(dic[i])
        return result
        