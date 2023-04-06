class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        hash_table = {}

        # Add each element to the hash table
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1

        # Check if num+k exists in the hash table
        for num in nums:
            if num + k in hash_table:
                count += hash_table[num + k]

        # Return the count
        return count