class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i,n in enumerate(nums):
            nums[i]=str(n)
        def compare(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1
        nums=sorted(nums,key=cmp_to_key(compare))
        #[0,0,0]="000" must be retured as "0" so to do this first we convert it to int then to string
        return str(int("".join(nums)))
       
            
        