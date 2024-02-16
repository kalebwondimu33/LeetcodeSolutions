class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hashtable=Counter(answers)
        total=0
        for num in hashtable:
            temp=num+1
            total+=(ceil(hashtable[num]/temp))*temp
        return total

        