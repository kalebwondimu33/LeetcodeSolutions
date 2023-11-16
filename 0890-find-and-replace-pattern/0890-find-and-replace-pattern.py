class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result=[]
        
        for word in words:
            if len(set(word))==len(set(pattern)):
                dic={}
                flag=False
                for j in range(len(pattern)):
                    if pattern[j] not in dic:
                        flag=True
                        dic[pattern[j]]=word[j]
                    elif pattern[j] in dic and dic[pattern[j]]!=word[j]:
                        flag=False
                        break
                if flag:
                    result.append(word)
        return result
                    
                
                
        