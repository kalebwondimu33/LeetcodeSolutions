class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]
        deque = collections.deque()
        res = n + 1
        for i in range(n + 1):
            while deque and presum[i] - presum[deque[0]] >= k:
                res = min(res, i - deque.popleft())
            while deque and presum[i] <= presum[deque[-1]]:
                deque.pop()
            deque.append(i)
        return res if res <= n else -1

        