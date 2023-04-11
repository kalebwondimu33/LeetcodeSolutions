class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=s.split()
        output=""
        for i in range(k):
            output+=words[i]
            output+=" "
        return output.rstrip()
            
        