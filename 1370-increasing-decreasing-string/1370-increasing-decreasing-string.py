class Solution:
    def sortString(self, s: str) -> str:
        count=sorted([k,v] for k,v in Counter(s).items())
        result=[]
        while len(result)<len(s):
            for i in range(len(count)):
                if count[i][1]:
                    result.append(count[i][0])
                    count[i][1]-=1
            for i in range(len(count)):
                if count[~i][1]:
                    result.append(count[~i][0])
                    count[~i][1]-=1
        return ''.join(result)
        
        