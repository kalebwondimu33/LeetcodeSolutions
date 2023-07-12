class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hashtable={}
        for i in range(lowLimit,highLimit+1):
            ball=str(i)
            digit_sum=sum(int(i) for i in ball)
            if digit_sum not in hashtable:
                hashtable[digit_sum]=1
            else:
                hashtable[digit_sum]+=1
        return max(hashtable.values())
        