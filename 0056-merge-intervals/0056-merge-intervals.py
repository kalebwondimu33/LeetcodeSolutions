class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        pre=intervals[0]
        res=[]
        for s,e in intervals[1:]:
            if s>pre[1]:
                res.append(pre)
                pre=[s,e]
            else:
                pre=[min(pre[0],s),max(pre[1],e)]
        res.append(pre)
        return res