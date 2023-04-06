class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result=[]
        numlist=[]
        num1=int(s[1])
        num2=int(s[4])
        for i in range(num1,num2+1):
            numlist.append(i) 
        char1=ord(s[0])
        char2=ord(s[3])
        for i in range(char1,char2+1):
            for j in numlist:
                first=chr(i)+f"{j}"
                result.append(first)
        return result