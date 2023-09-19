class Solution:
    def dayOfTheWeek(self, d: int, m: int, y: int) -> str:
        return date(y,m,d).strftime("%A")
        