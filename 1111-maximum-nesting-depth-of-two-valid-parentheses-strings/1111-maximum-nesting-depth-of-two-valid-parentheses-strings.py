class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        output=[]
        prev="B"
        for i in seq:
            if i=="(":
                if prev=="A":
                    output.append(1)
                    prev="B"
                else:
                    output.append(0)
                    prev="A"
            else:
                if prev=="A":
                    output.append(0)
                    prev="B"
                else:
                    output.append(1)
                    prev="A"
        return output