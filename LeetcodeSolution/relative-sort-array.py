class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count1=Counter(arr1)
        count2=Counter(arr2)
        ans=[]
        nn=[]
        for i in arr2:
            for j in range(count1[i]):
                ans.append(i)
        for k in count1:
            if k not in count2:
                for i in range(count1[k]):
                    nn.append(k)
        nn.sort()
        for n in nn:
            ans.append(n)
            
        return ans