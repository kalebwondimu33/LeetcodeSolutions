class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1=len(word1)
        length2=len(word2)
        output=""
        left=0
        right=0
        while left<length1 and right<length2:
            output+=word1[left]
            output+=word2[right]
            left+=1
            right+=1
        if length2>length1:
            output+=word2[right:]
        if length2<length1:
            output+=word1[left:]
        return output
            
            
            
            
        