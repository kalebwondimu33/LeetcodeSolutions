class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_p=Counter(p)
        k=len(p)
        window_dic=Counter(s[:k])
        ans=[]
        l=0
        r=k
        if window_dic==dic_p:
                ans.append(0)
        while r<len(s):
            window_dic[s[l]]-=1
            if window_dic[s[l]]==0:
                window_dic.pop(s[l])
            if s[r] in window_dic:
                window_dic[s[r]]+=1
            if s[r] not in window_dic:
                window_dic[s[r]]=1
            print(window_dic)
            if window_dic==dic_p:
                ans.append(l+1)
            l+=1
            r+=1
        return ans
            

        
           


                


        
        