class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word=text.split()
        count=0
        for i in word:
            flag=True
            for j in i:
                if j in brokenLetters:
                    flag=False
            if flag==True:
                count+=1
                
        return count
                    
        