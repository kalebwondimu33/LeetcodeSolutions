class RandomizedSet:

    def __init__(self):
        # Dict to track index of nums in nums list 
        self.toIndex = { }
        self.nums = collections.deque()

    def insert(self, val: int) -> bool:
        # If a number already exists then don't add it 
        if val in self.toIndex: return False
        # Else add the number to nums and save its index in map
        self.nums.append(val)
        self.toIndex[val] = len(self.nums) - 1
        
        return True

    def remove(self, val: int) -> bool:
        # If number not in map then number does not exist 
        if val not in self.toIndex: return False 

        # Move the number to be removed to last index of nums so it 
        # can be popped in O(1). 
        # When we move number to be deleted to the end, we will also have to 
        # update the index of the number that was origninally at the end 
        oldIndex, numAtEnd = self.toIndex[val], self.nums[-1]
        # Swap num to be deleted with last number in list 
        self.nums[oldIndex], self.nums[-1] = self.nums[-1], self.nums[oldIndex]
        # Update the index of number to be deleted (this also handles the situation
        # where deleted number already at end)
        self.toIndex[numAtEnd] = oldIndex 
        # Remove last number in list and remove its entry from tha map 
        self.nums.pop()
        del self.toIndex[val]        

        return True 

    def getRandom(self) -> int:
        # Choose a random index between 0 and len(list) and 
        # then return a number at that index
        n = len(self.nums)
        randInd = random.randrange(0, n)
        return self.nums[randInd]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()