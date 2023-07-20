class Solution:
    def countVowelStrings(self, n: int) -> int:
        ans=[1]*5
        for i in range(n):
            for i in range(len(ans)-2,-1,-1):
                ans[i]+=ans[i+1]
        return ans[0]
        