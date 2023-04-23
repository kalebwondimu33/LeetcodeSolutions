class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        word1=Counter(words1)
        word2=Counter(words2)
        count=0
        for i in words1:
            if word1[i]==1 and word2[i]==1:
                count+=1
        return count
                
        