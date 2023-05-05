class Solution:
    def reformatNumber(self, number: str) -> str:
        ss=number.replace(" ","").replace("-","")
        answer=[]
        while ss:
            if len(ss) == 2:
                answer.append(ss)
                break
            elif len(ss) == 4:
                answer.append(ss[:2])
                answer.append(ss[2:])
                break
            else:
                answer.append(ss[:3])
                ss = ss[3:]
        return "-".join(answer)
        