class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        pref_sum=[0]*(n+1)
        post_sum=[0]*(n+1)
        for i in range(1,n+1):
            pref_sum[i]=pref_sum[i-1]
            if customers[i-1]=="N":
                pref_sum[i]+=1
        for j in range(n-1,-1,-1):
            post_sum[j]=post_sum[j+1]
            if customers[j]=="Y":
                post_sum[j]+=1
        res=float("inf")
        indx=0
        for i in range(n+1):
            result=pref_sum[i]+post_sum[i]
            if result<res:
                res=result
                index=i
        return index
        


        



        
            

    
        