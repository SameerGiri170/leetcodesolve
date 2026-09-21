class Solution:
    def oddCells(self, m, n, indices):
        rows = [0] * m
        cols = [0] * n

        for r, c in indices:
            rows[r] += 1
            cols[c] += 1

        ans = 0

        for r in rows:
            for c in cols:
                if (r + c) % 2:
                    ans += 1

        return ans