class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        left=0
        right=0
        ans=0
        while left<len(seats):
            if seats[left]==students[right]:
                left+=1
                right+=1
            else:
                ans+=abs(seats[left]-students[right])
                right+=1
                left+=1
        return ans
            
        