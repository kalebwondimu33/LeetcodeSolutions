class ATM:

    def __init__(self):
        self.money = [0]*5
        self.order = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, amount in enumerate(banknotesCount):
            self.money[i] += amount

    def withdraw(self, amount: int) -> List[int]:
        output = [0]*5
        # We can start from i = 4 as len(answer) == 5 always and we need to go from the end to the start
        i = 4
        while amount and i >= 0:
            # We check for each value whether or not we will add all banknotes with this value we have or just some of them. 
            output[i] = min(self.money[i], amount//self.order[i])
            # Reduce rest amount with already used money
            amount -= output[i]*self.order[i]
            i -= 1
             
        if amount:
            # If we still have some uncovered amount after iteration, we should return [-1]
            return [-1]
        else:
            # Else we should update amount of banknotes and return banknotes we gave 
            for i, mon in enumerate(self.money):
                self.money[i] = mon - output[i]
            return output
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)