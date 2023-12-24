class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        ans=[]
        for i in nums:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        for j in range(len(pos)):
            ans.append(pos[j])
            ans.append(neg[j])
        return ans
            