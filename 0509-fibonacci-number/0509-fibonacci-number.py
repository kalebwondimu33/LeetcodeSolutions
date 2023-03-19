class Solution:
    def fib(self, n: int) -> int:
        hashtable={0:0,1:1}
        if n in hashtable:
            return hashtable[n]
        else:
            hashtable[n]=self.fib(n-1)+self.fib(n-2)
            return hashtable[n]
        