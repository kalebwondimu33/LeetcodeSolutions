class Solution:
    def countTestedDevices(self, bs: List[int]) -> int:
        tested_device=0
        for i in range(len(bs)):
            if bs[i]>0:
                tested_device+=1
                for j in range(i+1,len(bs)):
                    bs[j]=max(0,bs[j]-1)
        return tested_device
        