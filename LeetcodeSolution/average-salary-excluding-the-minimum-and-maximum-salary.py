class Solution:
    def average(self, salary: List[int]) -> float:
        small=min(salary)
        large=max(salary)
        sm_la=small+large
        num=len(salary)-2
        total=sum(salary)-sm_la
        return total/num
        