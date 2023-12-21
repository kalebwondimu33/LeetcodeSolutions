class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        table={"1":"QWERTYUIOP" ,"2":"ASDFGHJKL","3":"ZXCVBNM"}
        result=[]
        for i in words:
            count=0
            if i[0].upper() in table["1"]:
                for j in i:
                    if j.upper() in table["1"]:
                        count+=1
                if count==len(i):
                    result.append(i)
            elif i[0].upper() in table["2"]:
                for j in i:
                    if j.upper() in table["2"]:
                        count+=1
                if count==len(i):
                    result.append(i)
            else:
                for j in i:
                    if j.upper() in table["3"]:
                        count+=1
                    if count==len(i):
                        result.append(i)
                        
        return result
                    
                
        