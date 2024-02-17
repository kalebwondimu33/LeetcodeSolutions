class Solution:
    def minimumSteps(self, s: str) -> int:
        arr=list(s)
        count=0
        ones=0
        for right in range(len(arr)):
            if arr[right]=='1':
                ones+=1
            elif arr[right]=='0':
                count+=ones
        return count