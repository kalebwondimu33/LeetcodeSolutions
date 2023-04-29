class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1=Counter(word1)
        count2=Counter(word2)
        for i in count1:
            if abs(count1[i]-count2.get(i,0))>3:
                return False
        for j in count2:
            if abs(count1.get(j,0)-count2[j])>3:
                return False
        return True