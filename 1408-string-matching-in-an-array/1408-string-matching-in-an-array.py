class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                elif words[j] in words[i]:
                    ans.append(words[j])
        return list(set(ans))
        