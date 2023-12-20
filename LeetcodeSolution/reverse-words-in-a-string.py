class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        word=s.split()
        word.reverse()
        return  ' '.join(word)
            
        