class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        count=0
        for i in strs:
            if i.isdigit():
                count=max(count,int(i))
            else:
                count=max(count,len(i))
        return count
                
        