class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*n
        for first,last,seat in bookings:
            first=first-1
            last=last-1
            ans[first]+=seat
            if last+1<n:
                ans[last+1]-=seat
        for i in range(1,n):
            ans[i]+=ans[i-1]
        return ans
        