class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            s=""
            for j in range(len(strs)):
                s+=strs[j][i]
            if s!=''.join(sorted(s)):
                count+=1
        return count
            
        