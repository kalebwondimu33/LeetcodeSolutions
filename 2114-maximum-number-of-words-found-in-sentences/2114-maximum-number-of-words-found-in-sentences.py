class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        greater=0
        for i in range(len(sentences)):
            result=sentences[i].split()
            greater=max(greater,len(result))
        return greater
        