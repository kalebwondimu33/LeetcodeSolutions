class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dic={"T":0,"F":0}
        left=0
        ans=0
        for r in range(len(answerKey)):
            dic[answerKey[r]]+=1
            if min(dic["T"],dic["F"])<=k:
                ans=max(ans,dic["T"]+dic["F"])
            else:
                dic[answerKey[left]]-=1
                left+=1
        return ans


        