class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            left=0
            while left<len(i):
                if i[left]==0:
                    i[left]=1
                    left+=1
                elif i[left]==1:
                    i[left]=0
                    left+=1
            lef=0
            right=len(i)-1
            while lef<=right:
                i[lef],i[right]=i[right],i[lef]
                lef+=1
                right-=1
        return image
        