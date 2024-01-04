class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # d={}
        # for i in range(len(names)):
        #     d[heights[i]]=names[i]
        # ans=[]
        for i in range(len(names)):
            maxx=heights[i]
            index=i
            for j in range(i+1,len(names)):
                if maxx<heights[j]:
                    maxx=heights[j]
                    index=j
            heights[i],heights[index]=heights[index],heights[i]
            names[i],names[index]=names[index],names[i]
        # for i in heights:
        #     ans.append(d[i])
        return names
            
            
                
        