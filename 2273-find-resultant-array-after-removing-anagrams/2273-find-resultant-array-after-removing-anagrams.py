class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # i=0
        # while True:
        #     if i==len(words)-1:
        #         break
        #     if ''.join(sorted(words[i]))==''.join(sorted(words[i+1])):
        #         words.pop(i+1)
        #         i-=1
        #     i+=1
        # return words
        sorted_num=[sorted(w) for w in words]
        for i in range(1,len(sorted_num)):
            if sorted_num[i-1]==sorted_num[i]:
                words[i]=None
        result=[]
        for i in words:
            if i !=None:
                result.append(i)
        return result
    
    
    
        