class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = []
        ans = []

        for i in range(len(nums)):
            while q and q[0] <= i - k:
                q.pop(0)

            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans