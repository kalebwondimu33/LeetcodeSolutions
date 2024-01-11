class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operation=float("inf")
        l=0
        r=k
        while l<r and r<=len(blocks):
            temp=blocks[l:r].count('W')
            min_operation=min(min_operation,temp)
            l+=1
            r+=1
        return min_operation

        

            


        