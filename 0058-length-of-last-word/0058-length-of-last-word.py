class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list=s.split()
        result=word_list[-1]
        return len(result)
        
        