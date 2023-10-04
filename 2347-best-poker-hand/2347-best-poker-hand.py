class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        dic_rank={}
        dic_suits={}
        for i in ranks:
            if i not in dic_rank:
                dic_rank[i]=1
            else:
                dic_rank[i]+=1
        for j in suits:
            if j not in dic_suits:
                dic_suits[j]=1
            else:
                dic_suits[j]+=1
        
        for i in dic_suits:
            if dic_suits[i]==5:
                return "Flush"
        maxx_rank=0
        for j in dic_rank:
            if dic_rank[j]>maxx_rank:
                maxx_rank=dic_rank[j]
        print(dic_rank)
        print(maxx_rank)
        if maxx_rank>=3:
            return "Three of a Kind"
        if maxx_rank==2:
            return "Pair"
        if maxx_rank==1:
            return "High Card"
        
        