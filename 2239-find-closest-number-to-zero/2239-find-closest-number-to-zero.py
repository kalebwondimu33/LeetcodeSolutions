class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        pos,neg=[],[]
        for i in nums:
            if i<0:
                neg.append(i)
            elif i>0:
                pos.append(i)
            else:
                return 0
        if not neg:
            return sorted(pos)[0]
        if not pos:
            return sorted(neg)[-1]
        if abs(sorted(neg)[-1])<sorted(pos)[0]:
            return sorted(neg)[-1]
        return sorted(pos)[0]
            
            
            
        
                                          