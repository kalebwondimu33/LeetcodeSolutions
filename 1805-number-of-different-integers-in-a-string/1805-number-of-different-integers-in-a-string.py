class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers=""
        answer=set()
        for i in word:
            if i.isdigit():
                numbers+=i
            else:
                numbers+=" "
        result=numbers.split()
        for i in result:
            answer.add(int(i))
        return len(answer)
        
        
        