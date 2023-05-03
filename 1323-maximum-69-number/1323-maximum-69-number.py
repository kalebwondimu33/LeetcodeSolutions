class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str=str(num)
        result=[]
        for i in num_str:
            result.append(i)
        for i in range(len(result)):
            if result[i]=="6":
                result[i]="9"
                return int("".join(result))
        return int(num)
                
        