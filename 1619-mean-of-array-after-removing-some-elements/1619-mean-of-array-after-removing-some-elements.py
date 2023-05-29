class Solution:
    def trimMean(self, arr: List[int]) -> float:
        x=arr.sort()
        len1=len(arr)
        y=len1//20
        sum1=sum(arr[y:len1-y])
        return sum1/(len1-2*y)
        
        