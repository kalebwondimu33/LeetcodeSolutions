class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for bill in bills:
            if bill==5:
                five+=1
            elif bill==10 and five>0:
                ten+=1
                five-=1
            elif bill==20:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                elif ten==0 and five>=3:
                    five-=3
                else:
                    return False
            else:
                return False
        return True
        