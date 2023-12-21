class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)  # Find common elements between both lists
        index_sum = {}
        for i, r in enumerate(list1):
            if r in common:
                index_sum[r] = i  # Store index sum of common elements in list1
        for i, r in enumerate(list2):
            if r in common:
                index_sum[r] += i  # Add index sum of common elements in list2
        min_sum = min(index_sum.values())  # Find minimum index sum
        return [r for r, s in index_sum.items() if s == min_sum]  # Return elements with minimum index sum