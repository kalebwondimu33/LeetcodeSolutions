class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[1]*len(boxes)
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]=="1":
                    count+=abs(i-j)
            result[i]=count
        return result
                    
        