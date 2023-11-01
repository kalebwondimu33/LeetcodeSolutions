class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        output=[]
        dic={}
        for i in cpdomains:
            temp=i.split()
            num=temp[0]
            strings=temp[1].split('.')
            jj=""
            for i in range(len(strings)-1,-1,-1):
                if i==len(strings)-1:
                    jj=strings[i]
                    if jj not in dic:
                        dic[jj]=[int(num),strings[i]]
                    else:
                        dic[jj][0]+=int(num)
                    
                else:
                    jj=strings[i]+"."+jj
                    if jj not in dic:
                        dic[jj]=[int(num),jj]
                    else:
                        dic[jj][0]+=int(num)
                    
        for i in dic:
            output.append(str(dic[i][0])+" "+dic[i][1])
        return output
                
            
                