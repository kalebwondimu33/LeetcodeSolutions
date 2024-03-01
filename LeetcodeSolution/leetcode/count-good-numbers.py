class Solution:
    def countGoodNumbers(self, n: int) -> int:
        prime=4
        eve=5
        if n%2==0:
            odd=n//2
            even=n//2
            return (pow(prime,odd,10**9+7)*pow(eve,even,10**9+7))%(10**9 + 7)
        else:
            odd=n//2
            even=(n//2)+(n%2)
            return (pow(prime,odd,10**9+7)*pow(eve,even,10**9+7))%(10**9 + 7)

        