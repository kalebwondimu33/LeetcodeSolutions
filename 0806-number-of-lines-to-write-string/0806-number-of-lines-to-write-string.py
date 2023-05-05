class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        counter=0
        line=1
        for i in s:
            if counter+widths[ord(i)-97]<=100:
                counter+=widths[ord(i)-97]
            else:
                counter=widths[ord(i)-97]
                line+=1
        return [line,counter]
    
        