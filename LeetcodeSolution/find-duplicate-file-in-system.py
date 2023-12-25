class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={}
        ans=[]
        for i in paths:
            temp=i.split()
            directory=temp[0]
            for j in range(1,len(temp)):
                file=temp[j].split(".")
                num=file[0]
                content=file[1]
                file_path=directory+"/"+num+"."+"txt"
                if content not in d:
                    d[content]=[file_path]
                else:
                    d[content].append(file_path)
        for k in d:
            if len(d[k])>1:
                ans.append(d[k])
        return ans
                
                
                
        
        
        