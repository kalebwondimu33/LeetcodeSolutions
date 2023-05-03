class Solution:
    def countPoints(self, rings: str) -> int:
        dic={"0":[],"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[]}
        stack=[]
        for i in  rings:
            if i.isdigit():
                dic[i].append(stack[-1])
            else:
                stack.append(i)
        count=0
        for i in dic:
            if "B" in dic[i]and "G" in dic[i] and "R" in dic[i]:
                count+=1
        return count