class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        count=0
        temp=capacity
        for i in range(len(plants)):
            if plants[i]<=capacity:
                capacity-=plants[i]
                count+=1
            elif plants[i]>capacity:
                count+=(i)
                capacity=temp
                count+=(i+1)
                capacity-=plants[i]
        return count
                
        