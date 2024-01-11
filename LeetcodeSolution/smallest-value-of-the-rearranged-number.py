class Solution:
    def smallestNumber(self, num: int) -> int:

        if num<0:
            temp=list(str(-1*num))
            temp.sort(reverse=True)
            return -1*int(''.join(temp))
        elif num==0:
            return 0
        else:
            temp=list(str(num))
            temp.sort()
            zero=0
            ans=""
            for i in range(len(temp)):
                if temp[i]!='0':
                    ans+=temp[i]
                elif temp[i]=='0':
                    zero+=1
            if zero:
                return int(ans[0]+"0"*zero+ans[1:])
            else:
                return int(ans)
                    




        