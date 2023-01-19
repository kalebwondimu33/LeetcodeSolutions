class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet=string.ascii_lowercase
        count=0
        for i in alphabet:
            if i in sentence:
                count+=1
            else:
                return False
        if count==26:
            return True
        