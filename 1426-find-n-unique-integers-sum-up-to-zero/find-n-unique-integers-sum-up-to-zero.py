class Solution:
    def sumZero(self, n: int):
        ans = []

        for i in range(1, n // 2 + 1):
            ans += [i, -i]

        if n % 2:
            ans.append(0)

        return ans