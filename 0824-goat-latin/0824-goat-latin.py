class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sen=sentence.split()
        result=[]
        j=1
        for i in sen:
            if i[0].lower() in "aeiou":
                result.append(i+"ma"+"a"*j)
                j+=1
            else:
                result.append(i[1:]+i[0]+"ma"+"a"*j)
                j+=1
        return ' '.join(result)
                