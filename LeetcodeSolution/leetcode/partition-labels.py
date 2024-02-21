class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index={}
        for i,ch in enumerate(s):
            last_index[ch]=i
        size=0
        end=0
        result=[]
        for i,ch in enumerate(s):
            size+=1
            end=max(end,last_index[ch])
            if end==i:
                result.append(size)
                size=0
        return result

        