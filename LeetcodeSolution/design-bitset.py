class Bitset:

    def __init__(self, size: int):
		# stores original bits True -> 1, False -> 0
        self.bit = [False for i in range(size)]
		# inverse list of self.bit
        self.bitinv = [True for i in range(size)]
		# counter of True
        self.ones = 0
		# counter of False (both are for self.bit)
        self.zeros = size
		# original size
        self.size = size

    def fix(self, idx: int) -> None:
		# if the bit is 0/False set the bit and update the counters bitinv stores opposite of self.bit every time
        if not self.bit[idx]:
            self.zeros -= 1
            self.ones += 1
        self.bit[idx] = True
        self.bitinv[idx] = False

    def unfix(self, idx: int) -> None:
		# if the bit is set unset the bit and update both the lists as mentioned above
        if self.bit[idx]:
            self.zeros += 1
            self.ones -= 1
        self.bit[idx] = False
        self.bitinv[idx] = True

    def flip(self) -> None:
		# changing the zeros counter to ones and vice versa.
        self.ones,self.zeros = self.zeros,self.ones
		# changing the list pointers now inverse list will be the main list i.e. self.bit will point towards self.bitinv and vice versa.
        self.bit,self.bitinv = self.bitinv,self.bit

    def all(self) -> bool:
		# return True if ones counter equal to size otherwise False.
        return self.ones == self.size

    def one(self) -> bool:
		# returns True if ones counter greater than zeros
        return self.ones > 0

    def count(self) -> int:
		# returns the number of ones
        return self.ones

    def toString(self) -> str:
		# appending 1 to string if it's True in self.bit otherwise 0
        ans = ''
        for bit in self.bit:
            if bit:
                ans += '1'
            else:
                ans += '0'
        return ans
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()